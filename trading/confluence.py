"""CONFLUENCE: Lewis's 3-indicator setup as two PAPER books (Lewis, 5 Nov; go/no-go review 16 Nov).
Signal on 1h closes (Kraken public OHLC): EMA 9/21 cross + Stoch RSI cross out of the extreme zone + Bollinger mid side,
all within 3 bars, with the 4h trend (EMA50) agreeing. Skips entries around high-impact USD news (ForexFactory feed).
Stop 1.5 x ATR(14), target 3R, 48h time stop. If stop and target hit in the same hour, counted as a stop.
Books:
  pionex : £200 pot, £20 risk per trade (Lewis 6 Nov; was £10), max 40x, margin = 30% of cash per trade (Lewis 6 Nov: 20-30% of capital in every trade), 3 open max.
  funded : FTMO-style 2-Step phase 1 on $10k: +10% target, 5% daily / 10% max loss. 1% risk, position at least 30% of balance (Lewis 6 Nov), 2 open, BTC+ETH only.
           Locks for the day at -2.5%. Pass/fail logged, then a fresh attempt starts.
Paper only: never places orders, needs no keys.
  python confluence.py live         # Actions every 2h: new closed bars -> paper trades -> Telegram + results
  python confluence.py backtest 365 # 1h Binance archive -> results/confluence_backtest.md
"""
import json, math, os, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
RES = HERE / "results"
STATE = RES / "confluence_state.json"
OUT = RES / "confluence.md"
TRADES = RES / "confluence_trades.csv"
PAIRS = {"BTC": "XBTUSD", "ETH": "ETHUSD", "SOL": "SOLUSD", "XRP": "XRPUSD", "DOGE": "XDGUSD",
         "ADA": "ADAUSD", "LINK": "LINKUSD", "AVAX": "AVAXUSD"}
FEE = 0.0005          # per side on notional (Pionex futures taker 0.05%; FTMO crypto commission is lower)
STOP_ATR, TARGET_R, MAX_HOURS, WINDOW = 1.5, 3.0, 48, 3
TREND, ZONE = True, 30  # 4h EMA50 filter on/off; Stoch RSI extreme zone (30 = cross up from <30 / down from >70). sweep.py varies these.
BOOKS = {
    "pionex": {"start": 200.0, "cur": "£", "risk": 20.0, "max_lev": 40, "margin_pct": 0.30, "max_open": 3,
               "coins": list(PAIRS), "kill": 100.0},
    "pionex_majors": {"start": 200.0, "cur": "£", "risk": 20.0, "max_lev": 40, "margin_pct": 0.30, "max_open": 2,
                      "coins": ["BTC", "ETH"], "kill": 100.0},  # 5 Nov: year test BTC+ETH only = +£104 (53 trades)
    "funded": {"start": 10000.0, "cur": "$", "risk_pct": 0.01, "min_pos": 0.30, "max_lev": 3,  # min_pos: Lewis 6 Nov, >=20-30% of capital in every trade
               "max_open": 2, "coins": ["BTC", "ETH"],
               "target": 0.10, "daily": 0.05, "maxloss": 0.10, "day_lock": 0.025, "min_days": 4},
}
# Per-book settings (Lewis 12 Nov: "increase efficiency, we don't have a year"). Picked from results/sweep_confluence.md
# (730 days, profitable in train AND test halves, survives 2x fees). Books without "p" use the globals above.
BOOKS["funded"]["p"] = {"STOP_ATR": 2.0, "TARGET_R": 4.0, "MAX_HOURS": 120, "WINDOW": 5, "TREND": False, "ZONE": 30}  # 9 pass/6 fail vs 3/1, ~2.5x the trades, max DD 23%
BOOKS["funded"].update(press=1.5, press_cap=2.0)  # Lewis 12 Nov "capitalise on winners": risk 1% -> 1.5% after a win -> 2% cap; back to 1% after a loss. 730d: 10 pass/4 fail vs 9/6, better in BOTH halves. Flip-on-opposite-signal tested worse (7/5): left off.
BOOKS["pionex_majors"]["p"] = {"STOP_ATR": 2.0, "TARGET_R": 8.0, "MAX_HOURS": 48, "WINDOW": 3, "TREND": True, "ZONE": 30}  # +£885 vs +£598, 15/24 months up

def P(name, key):
    """Setting for one book: its own override, else the global (sweep.py sets the globals)."""
    return BOOKS[name].get("p", {}).get(key, globals()[key])

# ---------------- data + indicators ----------------

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "hq-bot"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def bars_1h(coin, forming=False):
    j = get(f"https://api.kraken.com/0/public/OHLC?pair={PAIRS[coin]}&interval=60")
    rows = next(v for k, v in j["result"].items() if k != "last")
    rows = rows if forming else rows[:-1]  # last row = the hour still forming
    return [{"t": int(r[0]), "o": float(r[1]), "h": float(r[2]), "l": float(r[3]), "c": float(r[4])} for r in rows]

def bars_hist(coin, days):
    """Backtest only: Binance public 1h archive (Kraken serves just 720 bars)."""
    sym = {"DOGE": "DOGEUSDT"}.get(coin, coin + "USDT")
    end, since, out = int(time.time() * 1000), int(time.time() * 1000) - days * 86_400_000, []
    while since < end:
        k = get(f"https://data-api.binance.vision/api/v3/klines?symbol={sym}&interval=1h&limit=1000&startTime={since}")
        if not k:
            break
        out += [{"t": r[0] // 1000, "o": float(r[1]), "h": float(r[2]), "l": float(r[3]), "c": float(r[4])} for r in k]
        since = k[-1][0] + 1
    return out[:-1]

def ema(xs, n):
    k, out, e = 2 / (n + 1), [], None
    for x in xs:
        e = x if e is None else x * k + e * (1 - k)
        out.append(e)
    return out

def sma(xs, n):
    return [None if i < n - 1 or any(v is None for v in xs[i - n + 1:i + 1]) else sum(xs[i - n + 1:i + 1]) / n
            for i in range(len(xs))]

def rsi(c, n=14):
    out, ag, al = [None] * len(c), 0.0, 0.0
    for i in range(1, len(c)):
        d = c[i] - c[i - 1]
        g, l = max(d, 0), max(-d, 0)
        if i <= n:
            ag += g / n; al += l / n
            if i < n:
                continue
        else:
            ag = (ag * (n - 1) + g) / n; al = (al * (n - 1) + l) / n
        out[i] = 100 if al == 0 else 100 - 100 / (1 + ag / al)
    return out

def stoch_rsi(c):
    r = rsi(c)
    raw = []
    for i in range(len(r)):
        w = r[max(0, i - 13):i + 1]
        if i < 27 or any(v is None for v in w):
            raw.append(None); continue
        lo, hi = min(w), max(w)
        raw.append(50.0 if hi == lo else 100 * (r[i] - lo) / (hi - lo))
    k = sma(raw, 3)
    return k, sma(k, 3)

def features(b):
    c = [x["c"] for x in b]
    f = {"e9": ema(c, 9), "e21": ema(c, 21), "mid": sma(c, 20)}
    f["sd"] = [None if i < 19 else math.sqrt(sum((v - f["mid"][i]) ** 2 for v in c[i - 19:i + 1]) / 20) for i in range(len(c))]
    f["k"], f["d"] = stoch_rsi(c)
    tr = [b[0]["h"] - b[0]["l"]] + [max(b[i]["h"] - b[i]["l"], abs(b[i]["h"] - c[i - 1]), abs(b[i]["l"] - c[i - 1]))
                                   for i in range(1, len(b))]
    f["atr"] = ema(tr, 27)  # Wilder 14 == EMA 27
    # 4h trend: close of each completed 4h block vs its EMA50, carried forward to the 1h bars after it
    blocks, last4 = {}, []
    for x in b:
        blocks.setdefault(x["t"] // 14400, []).append(x)
    keys = sorted(blocks)
    e4 = ema([blocks[k][-1]["c"] for k in keys], 50)
    trend = {k: (1 if blocks[k][-1]["c"] > e4[j] else -1) if j >= 50 else 0 for j, k in enumerate(keys)}
    f["trend"] = [trend.get(x["t"] // 14400 - 1, 0) for x in b]  # previous (closed) 4h block only
    return f

def signal(b, f, i, window=None, trend=None, zone=None):
    """+1 long / -1 short / 0. Uses bars up to and including i only. None = global setting."""
    WINDOW = globals()["WINDOW"] if window is None else window
    TREND = globals()["TREND"] if trend is None else trend
    ZONE = globals()["ZONE"] if zone is None else zone
    if i < 220 or f["k"][i] is None or f["d"][i - WINDOW] is None or f["sd"][i] is None:
        return 0
    for side in (1, -1):
        if TREND and f["trend"][i] != side:
            continue
        ema_x = any(side * (f["e9"][j] - f["e21"][j]) > 0 >= side * (f["e9"][j - 1] - f["e21"][j - 1])
                    for j in range(i - WINDOW + 1, i + 1))
        st_x = any(side * (f["k"][j] - f["d"][j]) > 0 >= side * (f["k"][j - 1] - f["d"][j - 1])
                   and (f["k"][j - 1] < ZONE if side == 1 else f["k"][j - 1] > 100 - ZONE) for j in range(i - WINDOW + 1, i + 1))
        bb = side * (b[i]["c"] - f["mid"][i]) > 0 and abs(b[i]["c"] - f["mid"][i]) < 2 * f["sd"][i]
        if ema_x and st_x and bb and side * (f["e9"][i] - f["e21"][i]) > 0:
            return side
    return 0

# ---------------- news filter ----------------

def news_windows():
    try:
        ev = get("https://nfs.faireconomy.media/ff_calendar_thisweek.json")
    except Exception as e:
        print("news feed failed, no filter this run:", e)
        return []
    out = []
    for e in ev:
        if e.get("impact") == "High" and e.get("country") == "USD":
            t = datetime.fromisoformat(e["date"]).timestamp()
            out.append([t - 3600, t + 1800, e.get("title", "")])
    return out

def blocked(t, wins):
    return next((w[2] for w in wins if w[0] <= t <= w[1]), None)

# ---------------- paper books ----------------

def new_book(name):
    cfg = BOOKS[name]
    return {"cash": cfg["start"], "open": [], "closed": [], "day": None, "day_start": cfg["start"],
            "attempt": 1, "attempt_start": cfg["start"], "days_traded": [], "results": [], "locked_day": None}

def day_of(t):
    return datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%d")

def try_open(name, bk, coin, side, bar, atr, t, events):
    cfg = BOOKS[name]
    if len(bk["open"]) >= cfg["max_open"] or any(p["coin"] == coin for p in bk["open"]):
        return
    if name.startswith("funded") and bk["locked_day"] == day_of(t):
        return
    if name.startswith("pionex") and bk["cash"] <= cfg["kill"]:
        return
    entry = bar["c"]
    stop_pct = P(name, "STOP_ATR") * atr / entry
    risk = cfg["risk"] if name.startswith("pionex") else cfg["risk_pct"] * bk["attempt_start"]
    if cfg.get("press"):  # Lewis 12 Nov: press winners: size up after a win, back to base after a loss
        last = [x for x in bk["closed"] if x["coin"] in cfg["coins"]][-1:]
        streak = bk.get("streak", 0) if last and last[0]["pnl"] > 0 else 0
        risk *= min(cfg["press"] ** streak, cfg.get("press_cap", 2.0))
    notional = risk / (stop_pct + 2 * FEE)
    if name.startswith("pionex"):
        free = bk["cash"] - sum(p["margin"] for p in bk["open"])
        margin = min(cfg["margin_pct"] * bk["cash"], free)
        if margin <= 1:
            return
        notional = min(notional, margin * cfg["max_lev"])
        lev = notional / margin
        if stop_pct >= 0.8 / lev:  # liquidation must sit well beyond the stop
            return
    else:
        notional = min(max(notional, cfg["min_pos"] * bk["cash"]), cfg["max_lev"] * bk["cash"])
        margin, lev = notional / cfg["max_lev"], cfg["max_lev"]
    p = {"coin": coin, "side": side, "t": t, "entry": entry, "notional": round(notional, 2), "margin": round(margin, 2),
         "lev": round(lev, 1), "stop": entry * (1 - side * stop_pct),
         "target": entry * (1 + side * stop_pct * P(name, "TARGET_R")), "risk": round(notional * (stop_pct + 2 * FEE), 2),
         "tr": P(name, "TARGET_R"), "max_h": P(name, "MAX_HOURS")}
    bk["open"].append(p)
    events.append(f"{name.upper()} OPEN {coin} {'LONG' if side > 0 else 'SHORT'} @ {entry:.6g} | stop {p['stop']:.6g} "
                  f"| target {p['target']:.6g} | {p['lev']}x, margin {cfg['cur']}{margin:.0f}, risk {cfg['cur']}{p['risk']:.2f}")

def close(name, bk, p, px, t, why, events):
    cfg = BOOKS[name]
    move = p["side"] * (px - p["entry"]) / p["entry"]
    pnl = p["notional"] * move - p["notional"] * FEE * 2  # fee in + fee out
    bk["cash"] += pnl
    bk["open"].remove(p)
    tr = {"book": name, "attempt": bk["attempt"], "coin": p["coin"], "side": "long" if p["side"] > 0 else "short",
          "open": datetime.fromtimestamp(p["t"], timezone.utc).strftime("%Y-%m-%d %H:%M"),
          "close": datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%d %H:%M"),
          "entry": round(p["entry"], 6), "exit": round(px, 6), "lev": p["lev"], "pnl": round(pnl, 2), "why": why,
          "balance": round(bk["cash"], 2)}
    bk["closed"].append(tr)
    bk["streak"] = bk.get("streak", 0) + 1 if pnl > 0 else 0
    d = day_of(p["t"])
    if d not in bk["days_traded"]:
        bk["days_traded"].append(d)
    events.append(f"{name.upper()} CLOSE {p['coin']} {why}: {'+' if pnl >= 0 else '-'}{cfg['cur']}{abs(pnl):.2f} "
                  f"| balance {cfg['cur']}{bk['cash']:.2f}")

def manage(name, bk, coin, bar, events):
    for p in [q for q in bk["open"] if q["coin"] == coin]:
        s = p["side"]
        if (s > 0 and bar["l"] <= p["stop"]) or (s < 0 and bar["h"] >= p["stop"]):
            close(name, bk, p, p["stop"], bar["t"] + 3600, "stop", events)
        elif (s > 0 and bar["h"] >= p["target"]) or (s < 0 and bar["l"] <= p["target"]):
            close(name, bk, p, p["target"], bar["t"] + 3600, f"target {p.get('tr', TARGET_R):g}R", events)
        elif bar["t"] + 3600 - p["t"] >= p.get("max_h", MAX_HOURS) * 3600:
            close(name, bk, p, bar["c"], bar["t"] + 3600, f"{p.get('max_h', MAX_HOURS)}h time stop", events)

def prop_rules(bk, t, events, marks, name="funded"):
    """FTMO checks on equity (cash + floating), once per closed hour."""
    cfg = BOOKS[name]
    d = day_of(t)
    if bk["day"] != d:
        bk["day"], bk["day_start"] = d, bk["cash"]
    eq = bk["cash"] + sum(p["notional"] * p["side"] * (marks.get(p["coin"], p["entry"]) - p["entry"]) / p["entry"]
                          for p in bk["open"])
    a0 = bk["attempt_start"]
    verdict = None
    if eq <= bk["day_start"] - cfg["daily"] * a0:
        verdict = "FAIL (5% daily loss)"
    elif eq <= a0 * (1 - cfg["maxloss"]):
        verdict = "FAIL (10% max loss)"
    elif bk["cash"] >= a0 * (1 + cfg["target"]) and not bk["open"] and len(bk["days_traded"]) >= cfg["min_days"]:
        verdict = "PASS (+10%)"
    elif eq <= bk["day_start"] - cfg["day_lock"] * a0 and bk["locked_day"] != d:
        bk["locked_day"] = d
        events.append(f"{name.upper()}: down 2.5% today, no new trades until tomorrow")
    if verdict:
        for p in list(bk["open"]):
            close(name, bk, p, marks.get(p["coin"], p["entry"]), t, "closed by prop rule", events)
        bk["results"].append({"attempt": bk["attempt"], "end": d, "verdict": verdict, "balance": round(bk["cash"], 2),
                              "trades": sum(1 for x in bk["closed"] if x["attempt"] == bk["attempt"])})
        events.append(f"{name.upper()} attempt {bk['attempt']}: {verdict}, balance ${bk['cash']:.0f}. Starting a fresh $10k attempt.")
        bk.update({"cash": cfg["start"], "attempt": bk["attempt"] + 1, "attempt_start": cfg["start"], "days_traded": [],
                   "day_start": cfg["start"], "open": [], "locked_day": None})

def step(books, data, feats, t, wins, events):
    """Process the 1h bar that opened at t, for every coin."""
    marks = {}
    for coin, b in data.items():
        i = feats[coin]["idx"].get(t)
        if i is None:
            continue
        bar, f = b[i], feats[coin]
        marks[coin] = bar["c"]
        for name, bk in books.items():
            if coin in BOOKS[name]["coins"]:
                manage(name, bk, coin, bar, events)
        why = None
        for name, bk in books.items():
            if coin not in BOOKS[name]["coins"]:
                continue
            side = signal(b, f, i, P(name, "WINDOW"), P(name, "TREND"), P(name, "ZONE"))
            if not side:
                continue
            if BOOKS[name].get("flip"):  # Lewis 12 Nov: flip on an opposite signal instead of waiting for stop/target
                for p in [q for q in bk["open"] if q["coin"] == coin and q["side"] == -side]:
                    close(name, bk, p, bar["c"], t + 3600, "flip", events)
            why = why or blocked(t + 3600, wins)
            if why:
                events.append(f"SKIP {coin} {name}: high-impact news ({why})")
                continue
            try_open(name, bk, coin, side, bar, f["atr"][i], t + 3600, events)
    for name, bk in books.items():
        if name.startswith("funded"):
            prop_rules(bk, t + 3600, events, marks, name)

def load(days=0):
    data = {c: (bars_hist(c, days) if days else bars_1h(c)) for c in PAIRS}
    feats = {}
    for c, b in data.items():
        feats[c] = features(b)
        feats[c]["idx"] = {x["t"]: i for i, x in enumerate(b)}
    return data, feats

# ---------------- outputs ----------------

def telegram(text):
    tok, chat = os.environ.get("TELEGRAM_TOKEN"), os.environ.get("OWNER_CHAT_ID")
    if tok and chat:
        try:
            data = urllib.parse.urlencode({"chat_id": chat, "text": text}).encode()
            urllib.request.urlopen(f"https://api.telegram.org/bot{tok}/sendMessage", data, timeout=30)
            return
        except Exception as e:
            print("telegram failed, using outbox:", e)
    sys.path.insert(0, str(HERE.parent / "village"))
    import tg_outbox
    tg_outbox.add(text)

def summary(name, bk):
    cfg, tr = BOOKS[name], bk["closed"]
    w = sum(t["pnl"] > 0 for t in tr)
    pnl = sum(t["pnl"] for t in tr)
    line = (f"**{name}**: {len(tr)} trades, {w} wins ({(w / len(tr) if tr else 0):.0%}), "
            f"P&L {'+' if pnl >= 0 else '-'}{cfg['cur']}{abs(pnl):.2f}, balance {cfg['cur']}{bk['cash']:.2f}, open {len(bk['open'])}")
    if name.startswith("funded"):
        line += f", attempt {bk['attempt']}; results: " + (", ".join(f"#{r['attempt']} {r['verdict']}" for r in bk["results"]) or "none yet")
    return line

def write_md(books, title, path):
    lines = [f"# {title}", f"Updated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC. Paper only.", ""]
    lines += ["- " + summary(n, bk) for n, bk in books.items()] + [""]
    for n, bk in books.items():
        lines += [f"## {n} last 15 trades", "| open | coin | side | lev | P&L | why |", "|---|---|---|---|---|---|"]
        lines += [f"| {t['open']} | {t['coin']} | {t['side']} | {t['lev']}x | {t['pnl']:+.2f} | {t['why']} |" for t in bk["closed"][-15:]]
        lines.append("")
    path.write_text("\n".join(lines))

def write_csv(books):
    cols = ["book", "attempt", "coin", "side", "open", "close", "entry", "exit", "lev", "pnl", "why", "balance"]
    rows = sorted((t for bk in books.values() for t in bk["closed"]), key=lambda t: t["close"])
    TRADES.write_text(",".join(cols) + "\n" + "".join(",".join(str(t[c]) for c in cols) + "\n" for t in rows))

# ---------------- modes ----------------

def all_times(data):
    return sorted({x["t"] for b in data.values() for x in b})

def backtest(days=365):
    data, feats = load(days)
    books = {n: new_book(n) for n in BOOKS}
    events = []
    for t in all_times(data):
        step(books, data, feats, t, [], events)
    write_md(books, f"CONFLUENCE backtest: last {days} days of 1h bars (Binance archive, no news filter)",
             RES / "confluence_backtest.md")
    for n, bk in books.items():
        print(summary(n, bk))

def live():
    data, feats = load()
    st = json.loads(STATE.read_text()) if STATE.exists() else None
    times = all_times(data)
    if not st:  # first run: start from now, no backfill
        st = {"last": times[-1], "books": {n: new_book(n) for n in BOOKS}}
    for n in BOOKS:
        st["books"].setdefault(n, new_book(n))
    books, events = st["books"], []
    wins = news_windows()
    for t in times:
        if t > st["last"]:
            step(books, data, feats, t, wins, events)
            st["last"] = t
    STATE.write_text(json.dumps(st, indent=1))
    write_md(books, "CONFLUENCE paper bots (BB + EMA cross + Stoch RSI)", OUT)
    write_csv(books)
    trades = [e for e in events if " OPEN " in e or " CLOSE " in e or "attempt" in e or "2.5%" in e]
    if trades:
        telegram("PAPER trades (no real money), your BB + EMA cross + Stoch RSI setup:\n" + "\n".join(trades)
                 + "\n\n" + "\n".join(summary(n, bk).replace("**", "") for n, bk in books.items()))
    print("\n".join(events) or "no new events")

def preview():
    """Heads-up ~10 min before the hour closes (server cron :50, Lewis 8 Nov 'get earlier to the punch').
    Checks the still-forming bar: if the setup would fire on the current price, Lewis gets entry/stop/target now
    instead of after the close. Not a trade: the paper books only act on closed bars. Deduped per coin per hour."""
    seen_f = Path(os.environ.get("PREVIEW_STATE", "/tmp/hq-confluence-preview.json"))
    seen = json.loads(seen_f.read_text()) if seen_f.exists() else {}
    wins, out = news_windows(), []
    for coin in PAIRS:
        try:
            b = bars_1h(coin, forming=True)
        except Exception as e:
            print("skip", coin, e)
            continue
        f, i = features(b), len(b) - 1
        side = signal(b, f, i)
        key = f"{coin}:{b[i]['t']}"
        if not side or key in seen or blocked(b[i]["t"] + 3600, wins):
            continue
        seen[key] = 1
        px, stop_pct = b[i]["c"], STOP_ATR * f["atr"][i] / b[i]["c"]
        books = [n for n, cfg in BOOKS.items() if coin in cfg["coins"]]
        out.append(f"{coin} {'LONG' if side > 0 else 'SHORT'} ~{px:.6g} | stop {px * (1 - side * stop_pct):.6g} "
                   f"| target {px * (1 + side * stop_pct * TARGET_R):.6g} | books: {', '.join(books)}")
    seen = {k: v for k, v in seen.items() if int(k.split(":")[1]) > time.time() - 86400}
    seen_f.write_text(json.dumps(seen))
    if out:
        telegram("HEADS-UP (hour not closed yet, setup forming on your BB + EMA + Stoch RSI):\n" + "\n".join(out)
                 + "\nConfirmed or cancelled at the top of the hour. Paper only.")
    print("\n".join(out) or "no setups forming")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "preview":
        preview()
        sys.exit()
    if len(sys.argv) > 1 and sys.argv[1] == "backtest":
        backtest(int(sys.argv[2]) if len(sys.argv) > 2 else 365)
    else:
        live()
