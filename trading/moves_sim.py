"""Big-move scenario farm (Lewis 17 Nov: "at least 100,000 scenarios", free compute in the public hq-sims repo).
115,200 scenarios = 360 signal sets x 320 exit sets, 10 coins, 2 years of Binance USDT-perp 1m data.
  signal: bar 1/3/5/15/30/60m x break of the last 12..288 bars' low/high x volume filter off/1.5/2/3/5x x follow/fade
  exit:   stop 0.5-3 ATR x take-profit none/1/2/3R x trailing on/off x hold 6/12/48/144 bars x entry market / limit pullback
Costs: Hyperliquid taker 0.045% + 0.02% slippage on market fills, maker 0.015% on limit entries and take-profits.
Conservative fills: stop wins if stop and target are both inside one bar; no take-profit on a limit's fill bar.
Overfit guard: periods A (oldest 50%, pick) / B (next 25%, confirm) / C (newest 25%, final). A scenario only counts if
it is up with t >= 2 in A AND B; C is the honest number. With 115k tries some pass A+B by luck: the report says how many.
  python moves_sim.py data [months]   -> data/moves/<COIN>.npz
  SHARD=i/n python moves_sim.py run   -> results/part_moves_<i>.json
  python moves_sim.py merge           -> results/moves_sim.md + results/moves_top.csv"""
import io, json, math, os, sys, zipfile, itertools, urllib.request
from datetime import date, timedelta, datetime, timezone
from pathlib import Path
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as swv

COINS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB", "ADA", "AVAX", "LINK", "SUI"]
if os.environ.get("UNIVERSE") == "50":  # 50-coin universe from tools/expand_simulation_universe.py
    COINS = json.load(open(Path(__file__).parent / "universe.json"))["coins"]
BARS, LOOK, VOLX, MODE = [1, 3, 5, 15, 30, 60], [12, 24, 48, 96, 192, 288], [0, 1.5, 2, 3, 5], ["follow", "fade"]
ENTRY, STOP_K, TP_R, TRAIL, HOLD = ["market", "limit"], [0.5, 1, 1.5, 2, 3], [0, 1, 2, 3], [0, 1], [6, 12, 48, 144]
TAKER, MAKER, COOL, HMAX, CHUNK = 0.00045 + 0.0002, 0.00015, 6, 144, 40_000
DATA, RES = Path(__file__).parent / "data" / "moves", Path(__file__).parent / "results"
SIGS = list(itertools.product(BARS, LOOK, VOLX, MODE))
EXITS = list(itertools.product(ENTRY, STOP_K, TP_R, TRAIL, HOLD))
XI = {e: j for j, e in enumerate(EXITS)}


# ---------------- data ----------------

def fetch(url):
    try:
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
    except Exception as e:
        print("skip", url, e); return None
    raw = z.read(z.namelist()[0]).decode()
    if not raw[:1].isdigit():
        raw = raw.split("\n", 1)[1]
    a = np.loadtxt(io.StringIO(raw), delimiter=",", usecols=(0, 2, 3, 4, 7), ndmin=2)
    a[:, 0] = np.where(a[:, 0] > 1e14, a[:, 0] // 1_000_000, a[:, 0] // 1000)  # ms or us -> seconds
    return a


def data(months=24):
    DATA.mkdir(parents=True, exist_ok=True)
    today = date.today(); first = today.replace(day=1)
    mons = [(first - timedelta(days=1 + 31 * k)).replace(day=1) for k in range(months)][::-1]
    base = "https://data.binance.vision/data/futures/um"
    for c in COINS:
        s = f"{c}USDT"
        urls = [f"{base}/monthly/klines/{s}/1m/{s}-1m-{m:%Y-%m}.zip" for m in sorted(set(mons))]
        urls += [f"{base}/daily/klines/{s}/1m/{s}-1m-{first + timedelta(days=d)}.zip" for d in range((today - first).days)]
        parts = [p for p in map(fetch, urls) if p is not None and len(p)]
        if not parts:
            continue
        a = np.concatenate(parts); a = a[np.unique(a[:, 0], return_index=True)[1]]
        np.savez_compressed(DATA / f"{c}.npz", t=a[:, 0].astype(np.int64), hlcv=a[:, 1:].astype(np.float32))
        print(c, len(a), "bars", datetime.fromtimestamp(a[0, 0], timezone.utc).date(), "->", datetime.fromtimestamp(a[-1, 0], timezone.utc).date())


def bars(t, hlcv, b):
    if b == 1:
        return t, hlcv[:, 0], hlcv[:, 1], hlcv[:, 2], hlcv[:, 3]
    k = t // (60 * b); cut = np.flatnonzero(np.diff(k)) + 1; st = np.r_[0, cut]; en = np.r_[cut, len(t)] - 1
    h, l, c, v = (hlcv[:, i] for i in range(4))
    return t[st], np.maximum.reduceat(h, st), np.minimum.reduceat(l, st), c[en], np.add.reduceat(v, st)


# ---------------- simulation ----------------

def signals(T, H, L, C, V, look, volx, mode):
    n = len(C)
    tr = np.maximum(H, np.r_[C[0], C[:-1]]) - np.minimum(L, np.r_[C[0], C[:-1]])
    cs = np.r_[0, np.cumsum(tr, dtype=np.float64)]; atr = np.full(n, np.nan); atr[13:] = (cs[14:] - cs[:-14]) / 14
    lo = np.full(n, np.nan); hi = np.full(n, np.nan)
    lo[look:] = swv(L, look).min(axis=1)[:-1]; hi[look:] = swv(H, look).max(axis=1)[:-1]
    ok = np.ones(n, bool)
    if volx:
        cv = np.r_[0, np.cumsum(V, dtype=np.float64)]; avg = np.full(n, np.nan); avg[48:] = (cv[48:-1] - cv[:-49]) / 48
        ok = V >= volx * avg
    side = np.where(C < lo, -1, np.where(C > hi, 1, 0)) * ok
    side[: max(look, 48)] = 0; side[n - HMAX - 4:] = 0; side[~(atr > 0)] = 0
    idx = np.flatnonzero(side)
    keep, last = [], -10 ** 9
    for i in idx:
        if i - last >= COOL:
            keep.append(i); last = i
    idx = np.array(keep, dtype=np.int64)
    s = side[idx] * (-1 if mode == "fade" else 1)
    return idx, s.astype(np.int8), atr[idx]


def paths(H, L, C, idx, s, atr, entry):
    """ATR-unit paths over the next HMAX bars: fav (best excursion), adv (worst), cls (close). Returns rows kept + entry price."""
    e = C[idx].astype(np.float64)
    start = idx + 1
    keep = np.ones(len(idx), bool)
    if entry == "limit":  # pullback 0.25 ATR toward the break within 3 bars, maker fill
        lvl = e - s * 0.25 * atr
        f = np.full(len(idx), -1)
        for d in (3, 2, 1):
            hit = np.where(s > 0, L[idx + d] <= lvl, H[idx + d] >= lvl)
            f[hit] = d
        keep = f > 0; e = lvl; start = idx + np.maximum(f, 1)
    W = lambda X: swv(X, HMAX)[start[keep]].astype(np.float32)
    Hw, Lw, Cw = W(H), W(L), W(C)
    ss, ee, aa = s[keep, None].astype(np.float32), e[keep, None].astype(np.float32), atr[keep, None].astype(np.float32)
    fav = np.where(ss > 0, Hw - ee, ee - Lw) / aa
    adv = np.where(ss > 0, Lw - ee, ee - Hw) / aa
    cls = ss * (Cw - ee) / aa
    if entry == "limit":
        fav[:, 0] = -1e9  # no take-profit on the fill bar (order inside the bar unknown)
    return keep, fav, adv, cls, (atr[keep] / e[keep]).astype(np.float64)


def first(m):
    has = m.any(axis=1)
    return np.where(has, m.argmax(axis=1), HMAX + 1)


def sim_set(coins, look, volx, mode, b, edges):
    """Stats per exit set: [nA,sA,qA,fA, nB,sB,qB,fB, nC,sC,qC,fC, nCshort,sCshort, nClong,sClong] (n, sum %, sum %^2, fee sum %)."""
    out = np.zeros((len(EXITS), 16))
    for T, H, L, C, V in coins:
        idx, s, atr = signals(T, H, L, C, V, look, volx, mode)
        for c0 in range(0, len(idx), CHUNK):
            ii, sx, ax = idx[c0:c0 + CHUNK], s[c0:c0 + CHUNK], atr[c0:c0 + CHUNK]
            for en in ENTRY:
                keep, fav, adv, cls, ap = paths(H, L, C, ii, sx, ax, en)
                if not len(ap):
                    continue
                per = np.searchsorted(edges, T[ii[keep]], side="right")  # 0=A 1=B 2=C
                side = sx[keep]
                fee_in = TAKER if en == "market" else MAKER
                best = np.maximum.accumulate(fav, axis=1); best = np.concatenate([np.zeros((len(ap), 1), np.float32), best[:, :-1]], axis=1)
                best = np.maximum(best, 0)
                rows = np.arange(len(ap))
                for k in STOP_K:
                    tps = {r: first(fav >= r * k) for r in TP_R if r}
                    for tr in TRAIL:
                        lvl = np.maximum(-k, best - k) if tr else np.full_like(adv, -k)
                        si = first(adv <= lvl); sv = lvl[rows, np.minimum(si, HMAX - 1)]
                        for r in TP_R:
                            ti = tps.get(r, np.full(len(ap), HMAX + 1))
                            for h in HOLD:
                                stop = (si < h) & (si <= ti); tp = (ti < h) & ~stop
                                ratr = np.where(stop, sv, np.where(tp, r * k, cls[:, h - 1]))
                                fee = fee_in + np.where(tp, MAKER, TAKER)
                                pnl = 100 * (ratr * ap - fee)
                                j = XI[(en, k, r, tr, h)]
                                for p in range(3):
                                    m = per == p
                                    if m.any():
                                        out[j, 4 * p:4 * p + 4] += (m.sum(), pnl[m].sum(), (pnl[m] ** 2).sum(), 100 * fee[m].sum())
                                m = per == 2
                                for q, sd in ((12, -1), (14, 1)):
                                    mm = m & (side == sd)
                                    out[j, q:q + 2] += (mm.sum(), pnl[mm].sum())
    return out


def run():
    i, n = map(int, os.environ.get("SHARD", "0/1").split("/"))
    raw = {c: np.load(f) for c, f in ((f.stem, f) for f in sorted(DATA.glob("*.npz")))}
    t0 = min(r["t"][0] for r in raw.values()); t1 = max(r["t"][-1] for r in raw.values())
    edges = np.array([t0 + (t1 - t0) * 0.5, t0 + (t1 - t0) * 0.75])
    mine = SIGS[i::n]; res = []
    for b in BARS:
        todo = [sg for sg in mine if sg[0] == b]
        if not todo:
            continue
        coins = [bars(r["t"], r["hlcv"], b) for r in raw.values()]
        for (_, look, volx, mode) in todo:
            st = sim_set(coins, look, volx, mode, b, edges)
            res.append({"sig": [b, look, volx, mode], "stats": np.round(st, 4).tolist()})
            print(f"shard {i}: {b}m N{look} vol{volx} {mode} done, {int(st[0, [0, 4, 8]].sum())} trades (first exit set)", flush=True)
    RES.mkdir(exist_ok=True)
    (RES / f"part_moves_{i}.json").write_text(json.dumps({"t0": int(t0), "t1": int(t1), "rows": res}))


# ---------------- report ----------------

def tstat(n, s, q):
    if n < 2:
        return 0.0, 0.0
    m = s / n; var = max(q / n - m * m, 1e-12) * n / (n - 1)
    return m, m / math.sqrt(var / n)


def merge():
    parts = [json.loads(p.read_text()) for p in sorted(RES.glob("part_moves_*.json"))]
    if not parts:
        print("no parts"); return
    t0 = min(p["t0"] for p in parts); t1 = max(p["t1"] for p in parts); days = (t1 - t0) / 86400
    dA, dB, dC = days * .5, days * .25, days * .25
    rows = []
    for p in parts:
        for r in p["rows"]:
            b, look, volx, mode = r["sig"]
            for (en, k, tp, tr, h), st in zip(EXITS, r["stats"]):
                mA, tA = tstat(*st[0:3]); mB, tB = tstat(*st[4:7]); mC, tC = tstat(*st[8:11])
                rows.append({"bar": b, "look": look, "vol": volx, "mode": mode, "entry": en, "stop": k, "tp": tp, "trail": tr, "hold": h,
                             "nA": st[0], "mA": mA, "tA": tA, "nB": st[4], "mB": mB, "tB": tB, "nC": st[8], "mC": mC, "tC": tC,
                             "mC2x": (st[9] - st[11]) / st[8] if st[8] else 0, "perdayC": st[8] / dC,
                             "shortC": st[13] / st[12] if st[12] else 0, "longC": st[15] / st[14] if st[14] else 0})
    tested = len(rows); live = [r for r in rows if r["nA"] >= 30 and r["nB"] >= 15 and r["nC"] >= 15]
    passA = [r for r in live if r["tA"] >= 2]
    passAB = [r for r in passA if r["tB"] >= 2]
    passABC = [r for r in passAB if r["tC"] >= 2]
    chance = len(live) * 0.023 * 0.023
    passAB.sort(key=lambda r: min(r["tA"], r["tB"]), reverse=True)
    fam = lambda key: {v: sum(1 for r in passAB if r[key] == v) for v in sorted({r[key] for r in rows}, key=str)}
    name = lambda r: (f"{r['bar']}m break {r['look']} bars, vol {'off' if not r['vol'] else str(r['vol']) + 'x'}, {r['mode']}, {r['entry']}, "
                      f"stop {r['stop']} ATR, TP {r['tp'] or 'none'}{'R' if r['tp'] else ''}, trail {'on' if r['trail'] else 'off'}, hold {r['hold']} bars")
    up = len(passABC)
    if up and len(passAB) > 2 * chance:
        verdict = (f"EDGE CANDIDATES: {up} scenarios were up (t>=2) in all three periods ({len(passAB)} passed the first two, ~{chance:.0f} "
                   "expected by luck). Next step: forward paper test the top ones before any money.")
    else:
        verdict = (f"NO RELIABLE EDGE: {len(passAB)} scenarios passed the pick + confirm periods (~{chance:.0f} by luck; similar scenarios "
                   f"share trades so they pass in clusters), and {up} held up in the newest period.")
    md = [f"# Big-move scenario farm ({tested:,} scenarios, {len(COINS)} coins, {days:.0f} days of 1m data)", "",
          f"**Verdict:** {verdict}", "",
          f"- Scenarios tested: {tested:,}; with enough trades in every period: {len(live):,}",
          f"- Up with t>=2 in A (oldest half, pick): {len(passA):,}",
          f"- ...and in B (next quarter, confirm): {len(passAB):,} (luck alone ~{chance:.0f}, rough: scenarios share trades)",
          f"- ...and in C (newest quarter, final): {up:,}",
          "- Costs: taker 0.045% + 0.02% slippage per market fill, maker 0.015%. 'C 2x' = C with costs doubled.", "",
          "Where the A+B survivors came from: " + "; ".join(f"{k}: {fam(k)}" for k in ("bar", "mode", "entry", "vol")), "",
          "## Top 30 A+B survivors and their final (C) result",
          "| scenario | A avg % (t) | B avg % (t) | **C avg %** (t) | C 2x costs | C trades/day | C shorts avg % | C longs avg % |",
          "|---|---|---|---|---|---|---|---|"]
    for r in passAB[:30]:
        md.append(f"| {name(r)} | {r['mA']:+.3f} ({r['tA']:.1f}) | {r['mB']:+.3f} ({r['tB']:.1f}) | **{r['mC']:+.3f}** ({r['tC']:.1f}) | "
                  f"{r['mC2x']:+.3f} | {r['perdayC']:.1f} | {r['shortC']:+.3f} | {r['longC']:+.3f} |")
    best = sorted(live, key=lambda r: r["mA"], reverse=True)[:5]
    md += ["", "## What picking the best-looking (A only) would have done",
           "| scenario | A avg % | C avg % |", "|---|---|---|"] + [f"| {name(r)} | {r['mA']:+.3f} | {r['mC']:+.3f} |" for r in best]
    md += ["", "Per trade % is of the position. At 30% of the account x 10x, account % per trade = 3x that."]
    (RES / "moves_sim.md").write_text("\n".join(md) + "\n")
    keys = list(rows[0])
    top = sorted(live, key=lambda r: min(r["tA"], r["tB"]), reverse=True)[:2000]
    (RES / "moves_top.csv").write_text(",".join(keys) + "\n" + "\n".join(",".join(f"{r[k]:.4f}" if isinstance(r[k], float) else str(r[k]) for k in keys) for r in top) + "\n")
    print("\n".join(md[:10]))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    if cmd == "data":
        data(int(sys.argv[2]) if len(sys.argv) > 2 else 24)
    elif cmd == "merge":
        merge()
    else:
        run()
