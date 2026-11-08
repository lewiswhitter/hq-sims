"""SMART race (Lewis 6 Nov, "whatever you recommend"): 4 strategies from the top-trader research, paper only.

Every strategy runs TWICE so sizing is tested too:
  <strat>_lewis : £200 pot, £20 stop per trade, 30% of cash as margin, up to 40x (Lewis's rules)
  <strat>_pro   : £200 pot, 1.5% risk per trade, max 5x (what top Hyperliquid traders use)

Strategies (all Hyperliquid public data, no keys, never places orders):
  copy    : top 15 Hyperliquid wallets by 30-day P&L (market makers filtered out). When 3+ more of them are
            long than short a coin (or vice versa), follow. Close when the crowd lets go. Live only (no history).
  trend   : 4h EMA 20/50 cross. Stop at the 10-bar swing low/high, target 2R, out on the opposite cross.
  bbsq    : 4h Bollinger squeeze breakout (bands inside Keltner 6+ bars, then a close outside). Stop 1.5 ATR, target 3R.
  movers  : 24h move of 8%+ still making new highs (long) or lows (short). Stop 2 ATR, target 3R, 24h max.
  squeeze : alt funding hunter. Crowded side (8h avg funding far from normal) + price breaks the 12h range
            against that crowd -> ride the squeeze. Stop 1.5 ATR, target 3R, 48h max.
  carry   : Ethena-style basis trade (Lewis research 6 Nov). Delta-neutral: long spot + short perp on the same coin,
            collect funding while the 24h average pays 15%+ a year, out when it drops under 3%. _pro = 1x, _lewis = 3x
            "looped" (forced out if price moves 30% from entry). Max 2 coins per book. Price risk ~0, funding/venue risk real.
  vcp     : Qullamaggie ADR/VCP breakout (Lewis research 6 Nov), long only. Coin with 5%+ average daily range, up 25%+
            off its 20-day low, range tightens (last 2 days under 60% of the 6 days before), then a 4h close breaks out.
            Stop = tight-range low (never wider than 1 ADR). Rides until a 4h close under the 20 EMA. Only trades when
            BTC is above its 4h 50 EMA (breadth filter: sit in cash in bear markets).
Book rules (all books): Millennium/Point72 drawdown cut. Once a book is 3%+ below its peak, risk per trade halves;
  6%+ below peak, quarter size. Full size again at a new peak. (Bridgewater vol sizing is already built in: fixed £ risk
  with an ATR stop = smaller positions on wilder coins.)
Coins: 15 liquid core coins + the 10 most volatile Robinhood coins (refreshed daily). Robinhood UK is buys-only.
Kill switch (live): total open interest down 10%+ in 24h AND average funding flipped positive -> negative
= leverage flush in progress, no new trades that run.

Usage: python smart.py backtest [days]   |   python smart.py live
"""
import csv, json, math, os, sys, time, urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
RES = HERE / "results"
STATE, OUT, TRADES = RES / "smart_state.json", RES / "smart.md", RES / "smart_trades.csv"
API = "https://api.hyperliquid.xyz/info"
LB = "https://stats-data.hyperliquid.xyz/Mainnet/leaderboard"
# Robinhood (US list, 6 Nov 2026) coins that also trade on Hyperliquid. Robinhood UK = spot only (via Bitstamp): buys only, no shorts.
ROBINHOOD = ["BTC", "ETH", "DOGE", "LTC", "kSHIB", "AAVE", "AERO", "ALGO", "ARB", "FET", "ASTER", "AVAX", "AVNT", "AXS", "BIO",
             "BCH", "BNB", "kBONK", "CC", "ADA", "CASHCAT", "LINK", "COMP", "ATOM", "CRV", "WIF", "EIGEN", "ENA", "ETC", "kFLOKI",
             "GRAM", "HBAR", "HYPE", "IMX", "INJ", "JTO", "ZRO", "LDO", "LIT", "MNT", "SYRUP", "MEGA", "MON", "MOODENG", "MORPHO",
             "NEAR", "TRUMP", "ONDO", "OP", "XPL", "DOT", "POPCAT", "PENGU", "PYTH", "SEI", "SKR", "SKY", "SOL", "STRK", "SUI", "XLM",
             "SNX", "UNI", "VVV", "VIRTUAL", "WLFI", "WLD", "ZORA", "XRP", "ZEC", "kPEPE"]
VOL_TOP, VOL_MIN_VLM = 10, 5e6   # add the 10 most volatile Robinhood coins (30d), min $5m/day volume on Hyperliquid
COINS = ["BTC", "ETH", "SOL", "HYPE", "XRP", "ZEC", "NEAR", "SUI", "ENA", "LINK", "WLD", "UNI", "kPEPE", "DOGE", "TRUMP"]
FEE = 0.0005  # per side (Pionex taker; Hyperliquid taker is 0.045%)
H = 3600
STRATS = {
    "copy":    {"tf": "1h", "target_r": 3.0, "max_h": 168, "live_only": True},
    "trend":   {"tf": "4h", "target_r": 2.0, "max_h": 360},
    "bbsq":    {"tf": "4h", "target_r": 3.0, "max_h": 120},
    "squeeze": {"tf": "1h", "target_r": 3.0, "max_h": 48},
    "movers":  {"tf": "1h", "target_r": 3.0, "max_h": 24},
    "carry":   {"tf": "1h", "target_r": 0, "max_h": 10_000},
    "vcp":     {"tf": "4h", "target_r": 20.0, "max_h": 720},   # trailing exit on the 20 EMA does the work
}
CARRY_LEV = {"lewis": 3.0, "pro": 1.0}
CARRY_IN, CARRY_OUT = 0.15 / 8760, 0.03 / 8760   # hourly funding = 15% / 3% a year
CARRY_MAX, CARRY_FLUSH = 2, 0.30
DD_STEPS = [(-0.06, 0.25), (-0.03, 0.5)]           # Millennium-style drawdown cut
SIZING = {
    "lewis": {"risk": 20.0, "margin_pct": 0.30, "max_lev": 40},
    "pro":   {"risk_pct": 0.015, "max_lev": 5},
}
POT, KILL, MAX_OPEN = 200.0, 100.0, 3
BBSQ_STOP, SQ_BARS, MOVERS_PCT = 1.5, 6, 0.08  # sweep.py varies these (8 Nov)
FUND_NORMAL = 0.0000125           # Hyperliquid baseline funding per hour (0.01% / 8h)
FUND_LONG_CROWD = 0.00005         # 8h average >= 4x normal: longs crowded
FUND_SHORT_CROWD = -0.00001       # 8h average below -0.001%/h: shorts crowded (negative is rare on HL)
COPY_TOP, COPY_NET, COPY_MIN_POS = 15, 3, 0.02
BOOKS = [f"{s}_{z}" for s in STRATS for z in SIZING]


# ---------------- data ----------------

def post(body, tries=6):
    for i in range(tries):
        try:
            req = urllib.request.Request(API, json.dumps(body).encode(), {"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(2 + 3 * i)

def candles(coin, tf, days):
    end = int(time.time() * 1000)
    rows = post({"type": "candleSnapshot", "req": {"coin": coin, "interval": tf,
                                                   "startTime": end - days * 86_400_000, "endTime": end}})
    step = 3600 if tf == "1h" else 14400
    out = [{"t": r["t"] // 1000, "o": float(r["o"]), "h": float(r["h"]), "l": float(r["l"]), "c": float(r["c"])} for r in rows]
    return [b for b in out if b["t"] + step <= end // 1000]  # closed bars only

def funding(coin, days):
    start, out = int(time.time() * 1000) - days * 86_400_000, {}
    while True:
        rows = post({"type": "fundingHistory", "coin": coin, "startTime": start})
        if not rows:
            break
        for r in rows:
            out[r["time"] // 1000 // H * H] = float(r["fundingRate"])
        if len(rows) < 500:
            break
        start = rows[-1]["time"] + 1
        time.sleep(0.3)
    return out

# ---------------- indicators ----------------

def ema(xs, n):
    k, out, e = 2 / (n + 1), [], None
    for x in xs:
        e = x if e is None else e + k * (x - e)
        out.append(e)
    return out

def atr(b, n=14):
    tr = [b[0]["h"] - b[0]["l"]] + [max(b[i]["h"] - b[i]["l"], abs(b[i]["h"] - b[i - 1]["c"]), abs(b[i]["l"] - b[i - 1]["c"]))
                                    for i in range(1, len(b))]
    return ema(tr, n)

def feats4h(b):
    c = [x["c"] for x in b]
    e20, e50, a = ema(c, 20), ema(c, 50), atr(b)
    mid, up, lo, sq = [], [], [], []
    for i in range(len(b)):
        w = c[max(0, i - 19): i + 1]
        m = sum(w) / len(w)
        sd = math.sqrt(sum((x - m) ** 2 for x in w) / len(w))
        mid.append(m); up.append(m + 2 * sd); lo.append(m - 2 * sd)
        sq.append(up[-1] < e20[i] + 1.5 * a[i] and lo[-1] > e20[i] - 1.5 * a[i])  # bands inside Keltner
    return {"e20": e20, "e50": e50, "atr": a, "mid": mid, "up": up, "lo": lo, "sq": sq}

def sig_trend(b, f, i):
    if i < 60:
        return 0, None
    if f["e20"][i - 1] <= f["e50"][i - 1] and f["e20"][i] > f["e50"][i]:
        return 1, min(x["l"] for x in b[i - 9: i + 1])
    if f["e20"][i - 1] >= f["e50"][i - 1] and f["e20"][i] < f["e50"][i]:
        return -1, max(x["h"] for x in b[i - 9: i + 1])
    return 0, None

def sig_bbsq(b, f, i):
    if i < 30 or not all(f["sq"][i - SQ_BARS: i]):
        return 0
    if b[i]["c"] > f["up"][i]:
        return 1
    if b[i]["c"] < f["lo"][i]:
        return -1
    return 0

def sig_movers(b, i, pct=None):
    """Big mover either way: 24h move of 8%+ that is still making new 24h highs (long) or lows (short)."""
    pct = MOVERS_PCT if pct is None else pct
    if i < 25:
        return 0
    ch = b[i]["c"] / b[i - 24]["c"] - 1
    if ch >= pct and b[i]["h"] >= max(x["h"] for x in b[i - 24: i]):
        return 1
    if ch <= -pct and b[i]["l"] <= min(x["l"] for x in b[i - 24: i]):
        return -1
    return 0

def sig_squeeze(b, i, fund):
    if i < 20:
        return 0
    rates = [fund.get(b[j]["t"]) for j in range(i - 7, i + 1)]
    rates = [r for r in rates if r is not None]
    if len(rates) < 6:
        return 0
    avg = sum(rates) / len(rates)
    hi, lo = max(x["h"] for x in b[i - 12: i]), min(x["l"] for x in b[i - 12: i])
    if avg <= FUND_SHORT_CROWD and b[i]["c"] > hi:
        return 1    # shorts crowded + price breaking up = short squeeze
    if avg >= FUND_LONG_CROWD and b[i]["c"] < lo:
        return -1   # longs crowded + price breaking down = long squeeze
    return 0

def adr(b, j, days=20):
    """Average daily range % from 4h bars (6 per day)."""
    rs = []
    for k in range(days):
        w = b[j - 6 * (k + 1) + 1: j - 6 * k + 1]
        if len(w) == 6:
            rs.append(max(x["h"] for x in w) / min(x["l"] for x in w) - 1)
    return sum(rs) / len(rs) if rs else 0

def sig_vcp(b, f, j, btc_ok):
    """Returns stop price for a long breakout, or None."""
    if j < 125 or not btc_ok:
        return None
    a = adr(b, j)
    if a < 0.05:
        return None
    tight, before = b[j - 12: j], b[j - 48: j - 12]
    rng = lambda w: max(x["h"] for x in w) / min(x["l"] for x in w) - 1
    c = b[j]["c"]
    if (rng(tight) < 0.6 * rng(before) and c > max(x["h"] for x in tight)
            and f["e20"][j] > f["e50"][j] and c > f["e20"][j]
            and c / min(x["l"] for x in b[j - 120: j]) - 1 >= 0.25):
        return max(min(x["l"] for x in tight), c * (1 - a))
    return None

def carry_step(books, coin, fund, t, px, events, allow_new):
    """Delta-neutral funding harvest. Hourly: accrue funding, check exits, maybe open."""
    rate = fund.get(t)
    avg = [fund.get(t - k * H) for k in range(24)]
    avg = [r for r in avg if r is not None]
    avg = sum(avg) / len(avg) if len(avg) >= 12 else None
    for z in SIZING:
        name, bk = f"carry_{z}", books[f"carry_{z}"]
        for p in [q for q in bk["open"] if q["coin"] == coin]:
            if rate is not None:
                p["earned"] = p.get("earned", 0.0) + p["notional"] * rate  # short perp receives positive funding
            moved = abs(px / p["entry"] - 1)
            if z == "lewis" and moved >= CARRY_FLUSH:
                close(name, bk, p, px, t + H, "forced deleverage", events)
            elif avg is not None and avg < CARRY_OUT:
                close(name, bk, p, px, t + H, "funding dried up", events)
        if (allow_new and avg is not None and avg >= CARRY_IN and bk["cash"] > KILL
                and len([q for q in bk["open"] if q.get("carry")]) < CARRY_MAX and not any(q["coin"] == coin for q in bk["open"])):
            notional = round(bk["cash"] * CARRY_LEV[z] / CARRY_MAX * dd_scale(bk), 2)
            # 4 legs (spot buy/sell + perp open/close): close() charges 2 x FEE, charge the spot pair up front
            bk["cash"] -= notional * FEE * 2
            bk["open"].append({"coin": coin, "side": 0, "t": t + H, "entry": px, "stop": 0, "target": 0, "carry": True,
                               "notional": notional, "margin": notional / CARRY_LEV[z], "lev": CARRY_LEV[z], "earned": 0.0})
            events.append(f"{name} OPEN {coin} CARRY (long spot + short perp) £{notional:.0f}, funding {avg * 8760:.0%}/yr")

# ---------------- books ----------------

def new_book():
    return {"cash": POT, "open": [], "closed": []}

def dd_scale(bk):
    dd = bk["cash"] / bk.get("peak", POT) - 1
    return next((m for lim, m in DD_STEPS if dd <= lim), 1.0)

def size(book_name, bk, entry, stop):
    """Returns (notional, margin, lev) or None. Paper maths only."""
    z = SIZING[book_name.rsplit("_", 1)[1]]
    stop_pct = abs(entry - stop) / entry
    if stop_pct <= 0.001 or bk["cash"] <= KILL:
        return None
    risk = (z["risk"] if "risk" in z else z["risk_pct"] * bk["cash"]) * dd_scale(bk)
    notional = risk / (stop_pct + 2 * FEE)
    used = sum(p["margin"] for p in bk["open"])
    if "margin_pct" in z:
        margin = min(z["margin_pct"] * bk["cash"], bk["cash"] - used)
        if margin <= 1:
            return None
        notional = min(notional, margin * z["max_lev"])
        lev = notional / margin
    else:
        notional = min(notional, z["max_lev"] * bk["cash"])
        lev = z["max_lev"]
        margin = notional / lev
        if margin > bk["cash"] - used:
            return None
    if stop_pct >= 0.8 / lev:  # stop must sit well inside the liquidation price
        return None
    return round(notional, 2), round(margin, 2), round(lev, 1)

def try_open(name, bk, coin, side, entry, stop, t, events):
    if len(bk["open"]) >= MAX_OPEN or any(p["coin"] == coin for p in bk["open"]):
        return
    s = size(name, bk, entry, stop)
    if not s:
        return
    notional, margin, lev = s
    r = abs(entry - stop)
    tgt = entry + side * r * STRATS[name.rsplit("_", 1)[0]]["target_r"]
    bk["open"].append({"coin": coin, "side": side, "t": t, "entry": entry, "stop": stop, "target": tgt,
                       "notional": notional, "margin": margin, "lev": lev})
    events.append(f"{name} OPEN {coin} {'LONG' if side > 0 else 'SHORT'} @ {entry:.6g} | stop {stop:.6g} | "
                  f"target {tgt:.6g} | {lev}x, margin £{margin:.0f}")

def close(name, bk, p, px, t, why, events):
    pnl = p["notional"] * p["side"] * (px - p["entry"]) / p["entry"] - p["notional"] * FEE * 2
    pnl = max(pnl, -p["margin"])  # can't lose more than the margin (liquidation)
    pnl += p.get("earned", 0.0)  # carry: funding collected
    bk["cash"] += pnl
    bk["peak"] = max(bk.get("peak", POT), bk["cash"])
    bk["open"].remove(p)
    ts = lambda x: datetime.fromtimestamp(x, timezone.utc).strftime("%Y-%m-%d %H:%M")
    bk["closed"].append({"book": name, "coin": p["coin"], "side": "carry" if p.get("carry") else "long" if p["side"] > 0 else "short", "open": ts(p["t"]),
                         "close": ts(t), "entry": round(p["entry"], 6), "exit": round(px, 6), "lev": p["lev"],
                         "pnl": round(pnl, 2), "why": why, "balance": round(bk["cash"], 2)})
    events.append(f"{name} CLOSE {p['coin']} {why}: {'+' if pnl >= 0 else '-'}£{abs(pnl):.2f} | balance £{bk['cash']:.2f}")

def manage(name, bk, coin, bar, events):
    for p in [q for q in bk["open"] if q["coin"] == coin and not q.get("carry")]:
        s, end = p["side"], bar["t"] + H
        if (s > 0 and bar["l"] <= p["stop"]) or (s < 0 and bar["h"] >= p["stop"]):
            close(name, bk, p, p["stop"], end, "stop", events)
        elif (s > 0 and bar["h"] >= p["target"]) or (s < 0 and bar["l"] <= p["target"]):
            close(name, bk, p, p["target"], end, "target", events)
        elif end - p["t"] >= STRATS[name.rsplit("_", 1)[0]]["max_h"] * H:
            close(name, bk, p, bar["c"], end, "time stop", events)

def exit_signal(strat, books, coin, side_now, px, t, events):
    """Strategy-specific exits (opposite trend cross, copy crowd let go)."""
    for z in SIZING:
        name = f"{strat}_{z}"
        for p in [q for q in books[name]["open"] if q["coin"] == coin and q["side"] != side_now]:
            close(name, books[name], p, px, t, "opposite signal" if strat == "trend" else "crowd let go", events)

# ---------------- step ----------------

def step(books, d, t, events, allow_new=True):
    """Process the 1h bar that opened at t, for every coin."""
    for coin in COINS:
        if coin not in d["i1"] or t not in d["i1"][coin]:
            continue
        b1, i = d["h1"][coin], d["i1"][coin][t]
        bar = b1[i]
        for name in BOOKS:
            manage(name, books[name], coin, bar, events)
        end = t + H
        carry_step(books, coin, d["fund"].get(coin, {}), t, bar["c"], events, allow_new)
        if end % 14400 == 0 and (end - 14400) in d["i4"].get(coin, {}):  # vcp trailing exit: 4h close under the 20 EMA
            j = d["i4"][coin][end - 14400]
            if d["h4"][coin][j]["c"] < d["f4"][coin]["e20"][j]:
                for z in SIZING:
                    for p in [q for q in books[f"vcp_{z}"]["open"] if q["coin"] == coin]:
                        close(f"vcp_{z}", books[f"vcp_{z}"], p, bar["c"], end, "lost 20 EMA", events)
        if not allow_new:
            continue
        s = sig_squeeze(b1, i, d["fund"].get(coin, {}))
        if s:
            a = atr(b1[max(0, i - 60): i + 1])[-1]
            for z in SIZING:
                try_open(f"squeeze_{z}", books[f"squeeze_{z}"], coin, s, bar["c"], bar["c"] - s * 1.5 * a, end, events)
        s = sig_movers(b1, i)
        if s:
            a = atr(b1[max(0, i - 60): i + 1])[-1]
            for z in SIZING:
                try_open(f"movers_{z}", books[f"movers_{z}"], coin, s, bar["c"], bar["c"] - s * 2 * a, end, events)
        if end % 14400 == 0 and (end - 14400) in d["i4"].get(coin, {}):  # a 4h bar just closed
            b4, f4, j = d["h4"][coin], d["f4"][coin], d["i4"][coin][end - 14400]
            s, swing = sig_trend(b4, f4, j)
            if s:
                exit_signal("trend", books, coin, s, bar["c"], end, events)
                a = f4["atr"][j]
                stop = min(max(abs(bar["c"] - swing), 0.5 * a), 3 * a)
                for z in SIZING:
                    try_open(f"trend_{z}", books[f"trend_{z}"], coin, s, bar["c"], bar["c"] - s * stop, end, events)
            bj = d["i4"].get("BTC", {}).get(end - 14400)
            btc_ok = bj is not None and d["h4"]["BTC"][bj]["c"] > d["f4"]["BTC"]["e50"][bj]
            stop = sig_vcp(b4, f4, j, btc_ok)
            if stop:
                for z in SIZING:
                    try_open(f"vcp_{z}", books[f"vcp_{z}"], coin, 1, bar["c"], stop, end, events)
            s = sig_bbsq(b4, f4, j)
            if s:
                a = f4["atr"][j]
                for z in SIZING:
                    try_open(f"bbsq_{z}", books[f"bbsq_{z}"], coin, s, bar["c"], bar["c"] - s * BBSQ_STOP * a, end, events)

def load(days, fund_days):
    d = {"h1": {}, "h4": {}, "f4": {}, "i1": {}, "i4": {}, "fund": {}}
    for c in COINS:
        try:
            d["h1"][c] = candles(c, "1h", days)
            d["h4"][c] = candles(c, "4h", days + 30)
            d["fund"][c] = funding(c, fund_days)
        except Exception as e:
            print("skip", c, e)
            continue
        d["f4"][c] = feats4h(d["h4"][c])
        d["i1"][c] = {x["t"]: k for k, x in enumerate(d["h1"][c])}
        d["i4"][c] = {x["t"]: k for k, x in enumerate(d["h4"][c])}
        time.sleep(0.3)
    return d

def volatile_coins():
    """Top Robinhood coins by 30-day daily volatility, liquid enough on Hyperliquid. Refreshed once a day."""
    meta, ctx = post({"type": "metaAndAssetCtxs"})
    vlm = {u["name"]: float(c["dayNtlVlm"]) for u, c in zip(meta["universe"], ctx) if not u.get("isDelisted")}
    rows = []
    for c in ROBINHOOD:
        if vlm.get(c, 0) < VOL_MIN_VLM:
            continue
        try:
            b = candles(c, "1d", 31)
        except Exception:
            continue
        if len(b) >= 20:
            r = [math.log(b[i]["c"] / b[i - 1]["c"]) for i in range(1, len(b))]
            rows.append((math.sqrt(sum(x * x for x in r) / len(r)), c))
        time.sleep(0.15)
    return [c for _, c in sorted(rows, reverse=True)[:VOL_TOP]]

# ---------------- copy (live only) ----------------

def top_wallets():
    req = urllib.request.Request(LB, headers={"User-Agent": "hq-bot"})
    with urllib.request.urlopen(req, timeout=120) as r:
        rows = json.loads(r.read())["leaderboardRows"]
    picks = []
    for r in rows:
        w = dict(r["windowPerformances"])
        av = float(r["accountValue"])
        m, wk, at = w["month"], w["week"], w["allTime"]
        if (av >= 100_000 and float(m["pnl"]) > 0 and float(m["roi"]) >= 0.10 and float(wk["pnl"]) > 0
                and float(at["pnl"]) > 0 and float(m["vlm"]) < 50 * av):  # huge volume vs size = market maker, skip
            picks.append((float(m["pnl"]), r["ethAddress"], round(float(m["roi"]), 3)))
    return [{"addr": a, "month_pnl": round(p), "month_roi": roi} for p, a, roi in sorted(picks, reverse=True)[:COPY_TOP]]

def crowd(wallets):
    net = defaultdict(int)
    for w in wallets:
        try:
            st = post({"type": "clearinghouseState", "user": w["addr"]})
        except Exception:
            continue
        av = float(st["marginSummary"]["accountValue"]) or 1
        for ap in st["assetPositions"]:
            p = ap["position"]
            if p["coin"] in COINS and abs(float(p["positionValue"])) >= COPY_MIN_POS * av:
                net[p["coin"]] += 1 if float(p["szi"]) > 0 else -1
        time.sleep(0.2)
    return dict(net)

def run_copy(books, net, d, t, events, allow_new):
    for coin in COINS:
        if coin not in d["h1"] or not d["h1"][coin]:
            continue
        n, px = net.get(coin, 0), d["h1"][coin][-1]["c"]
        side = 1 if n >= COPY_NET else -1 if n <= -COPY_NET else 0
        for z in SIZING:
            for p in [q for q in books[f"copy_{z}"]["open"] if q["coin"] == coin and q["side"] * n <= 0]:
                close(f"copy_{z}", books[f"copy_{z}"], p, px, t, "crowd let go", events)
        if side and allow_new:
            a = d["f4"][coin]["atr"][-1]
            for z in SIZING:
                try_open(f"copy_{z}", books[f"copy_{z}"], coin, side, px, px - side * 2 * a, t, events)

def kill_switch(st):
    """Leverage flush check from Hyperliquid's live open interest + funding. Returns reason or None."""
    meta, ctx = post({"type": "metaAndAssetCtxs"})
    oi = fsum = n = 0
    for u, c in zip(meta["universe"], ctx):
        if u["name"] in COINS:
            oi += float(c["openInterest"]) * float(c["markPx"])
            fsum += float(c["funding"]); n += 1
    now = int(time.time())
    hist = [h for h in st.get("oi_hist", []) if now - h[0] <= 30 * H] + [[now, oi, fsum / max(n, 1)]]
    st["oi_hist"] = hist
    old = [h for h in hist if now - h[0] >= 20 * H]
    if old and oi < 0.9 * old[0][1] and old[0][2] > 0 > fsum / max(n, 1):
        return f"open interest {oi / old[0][1] - 1:+.0%} in 24h and funding flipped negative"
    return None

def mood(d):
    """June 2026 check (best month by far): market-wide one-way move + high volatility = squeeze breakouts follow through."""
    up = n = 0; vol = []
    for c, b in d["h4"].items():
        if len(b) < 43:
            continue
        n += 1; up += b[-1]["c"] > b[-43]["c"]
        vol += [(x["h"] - x["l"]) / x["c"] for x in b[-42:]]
    if not n:
        return "Market mood: no data"
    v = sum(vol) / len(vol)
    june = (up <= 2 or up >= n - 2) and v >= 0.028
    return (f"Market mood (7d): {up}/{n} coins up, 4h range {v:.1%} (normal ~2-2.5%). "
            + ("JUNE-TYPE: one-way + volatile. Backtest: squeeze trades in this mood won 55% vs 36% (22 trades, small sample)." if june
               else "Normal mood: expect more fake breakouts."))

# ---------------- outputs ----------------

def months(tr):
    m = defaultdict(float)
    for x in tr:
        m[x["close"][:7]] += x["pnl"]
    return m

def summary(name, bk):
    tr = bk["closed"]
    w, pnl, m = sum(x["pnl"] > 0 for x in tr), sum(x["pnl"] for x in tr), months(tr)
    lp = sum(x["pnl"] for x in tr if x["side"] == "long")
    line = (f"{name}: {len(tr)} trades, {(w / len(tr) if tr else 0):.0%} wins, P&L {'+' if pnl >= 0 else '-'}£{abs(pnl):.2f} "
            f"(longs £{lp:+.0f}, shorts £{pnl - lp:+.0f}), balance £{bk['cash']:.2f}, open {len(bk['open'])}")
    if len(m) > 1:
        line += f" | per month avg £{sum(m.values()) / len(m):+.0f}, best £{max(m.values()):+.0f}, worst £{min(m.values()):+.0f}"
    return line

def write_md(books, title, path, extra=()):
    lines = [f"# {title}", f"Updated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC. Paper only, £200 pot per book.", ""]
    lines += list(extra) + [""] + ["- " + summary(n, books[n]) for n in BOOKS] + [""]
    for n in BOOKS:
        tr = books[n]["closed"][-10:]
        if tr:
            lines += [f"## {n} last 10", "| open | coin | side | lev | P&L | why |", "|---|---|---|---|---|---|"]
            lines += [f"| {x['open']} | {x['coin']} | {x['side']} | {x['lev']}x | {x['pnl']:+.2f} | {x['why']} |" for x in tr]
            lines.append("")
    path.write_text("\n".join(lines))

def write_csv(books):
    cols = ["book", "coin", "side", "open", "close", "entry", "exit", "lev", "pnl", "why", "balance"]
    rows = sorted((x for bk in books.values() for x in bk["closed"]), key=lambda x: x["close"])
    TRADES.write_text(",".join(cols) + "\n" + "".join(",".join(str(x[c]) for c in cols) + "\n" for x in rows))

def telegram(text):
    sys.path.insert(0, str(HERE))
    from confluence import telegram as tg
    tg(text)

# ---------------- modes ----------------

def backtest(days=200):
    d = load(days, days)
    books = {n: new_book() for n in BOOKS}
    events = []
    for t in sorted({x["t"] for b in d["h1"].values() for x in b}):
        step(books, d, t, events)
    write_md(books, f"SMART backtest: last {days} days, Hyperliquid 1h/4h + real funding (copy = live only)",
             RES / "smart_backtest.md")
    for n in BOOKS:
        if not STRATS[n.rsplit("_", 1)[0]].get("live_only"):
            print(summary(n, books[n]))

def live():
    st = json.loads(STATE.read_text()) if STATE.exists() else {}
    books = st.setdefault("books", {})
    for n in BOOKS:
        books.setdefault(n, new_book())
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if st.get("vol_day") != today:
        try:
            st["vol_coins"], st["vol_day"] = volatile_coins(), today
        except Exception as e:
            print("volatile list failed:", e)
    global COINS
    COINS = list(dict.fromkeys(COINS + [c for c in st.get("vol_coins", []) if c not in COINS]))
    d = load(10, 2)  # 4h bars cover 40 days
    events, now = [], int(time.time())
    try:
        why = kill_switch(st)
    except Exception as e:
        why, _ = None, print("kill switch check failed:", e)
    if why:
        events.append(f"KILL SWITCH: {why}. No new trades this run.")
    times = sorted({x["t"] for b in d["h1"].values() for x in b})
    last = st.get("last") or times[-1]  # first run: start from now
    for t in times:
        if t > last:
            step(books, d, t, events, allow_new=not why)
            st["last"] = t
    st.setdefault("last", last)
    if st.get("wallets_day") != today:
        try:
            st["wallets"], st["wallets_day"] = top_wallets(), today
        except Exception as e:
            print("leaderboard failed:", e)
    net = crowd(st.get("wallets", []))
    st["crowd"] = net
    run_copy(books, net, d, now, events, allow_new=not why)
    STATE.write_text(json.dumps(st, indent=1))
    crowd_line = "Top-wallet crowd (longs minus shorts): " + (", ".join(f"{c} {v:+d}" for c, v in sorted(net.items(), key=lambda x: -abs(x[1]))) or "none")
    mood_line = mood(d)
    write_md(books, "SMART paper race (copy / trend / Bollinger squeeze / funding squeeze / movers / carry / VCP, your sizing vs pro)", OUT,
             [mood_line, crowd_line, "Volatile Robinhood coins added today: " + (", ".join(st.get("vol_coins", [])) or "none"),
              f"Following {len(st.get('wallets', []))} wallets, refreshed daily."])
    write_csv(books)
    msg = []
    if events:
        rh = [e for e in events if " OPEN " in e and " LONG " in e and e.split(" OPEN ")[1].split()[0] in ROBINHOOD]
        msg.append("PAPER trades (no real money), SMART race:\n" + "\n".join(events)
                   + ("\nRobinhood UK can copy these (buys only): " + ", ".join(sorted({e.split(' OPEN ')[1].split()[0] for e in rh})) if rh else ""))
    if st.get("digest_day") != today and datetime.now(timezone.utc).hour >= 7:
        st["digest_day"] = today
        STATE.write_text(json.dumps(st, indent=1))
        msg.append("SMART race daily (paper, £200 each; _lewis = your sizing, _pro = 1.5% risk, 5x max):\n"
                   + "\n".join(summary(n, books[n]) for n in BOOKS) + "\n" + crowd_line + "\n" + mood_line
                   + "\nVolatile Robinhood coins in the race: " + ", ".join(st.get("vol_coins", [])))
    if msg:
        telegram("\n\n".join(msg))
    print("\n".join(events) or "no new events")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "backtest":
        backtest(int(sys.argv[2]) if len(sys.argv) > 2 else 200)
    else:
        live()
