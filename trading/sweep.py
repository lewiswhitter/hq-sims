"""SWEEP: mass simulation of Lewis's CONFLUENCE setup (Lewis 7 Nov: "run as many simulations as possible"; job 9c5cc0).
Runs on the Oracle server (2 cores, 12GB, idle), started by deploy/oracle_jobs.sh from Hetzner. Stdlib only. Paper maths only.

Grid over stop (ATR), target (R), time stop, signal window, 4h trend filter on/off and Stoch RSI zone,
for the three books that matter on 16 Nov: pionex (all coins), pionex_majors (BTC+ETH) and funded (FTMO 2-Step sim).
Walk-forward: every setting is scored on the first 2/3 of the data (train) and the last 1/3 (test) separately.
A setting only counts as "passes" if BOTH halves make money, and it still makes money at double fees.

Suites (8 Nov, Lewis "we still have more capacity, use it"):
  confluence : 1,728 settings x pionex / pionex_majors / funded, 730 days Binance 1h
  smart      : 1,296 settings of SMART bbsq / movers / trend, 200 days Hyperliquid 1h+4h with real funding
  python sweep.py [suite|all] [days] [workers]   -> results/sweep_<suite>.md + .csv
Oracle runs `all` back to back, then again every day (fresh data = fresh walk-forward).
"""
import csv, itertools, json, os, sys, time
from datetime import datetime, timezone
from multiprocessing import Pool
from pathlib import Path

import confluence as C

HERE = Path(__file__).parent
CACHE = HERE / "data"
GRID = {
    "STOP_ATR": [1.0, 1.5, 2.0, 2.5, 3.0, 4.0],
    "TARGET_R": [1.5, 2.0, 3.0, 4.0, 5.0, 8.0],
    "MAX_HOURS": [24, 48, 120],
    "WINDOW": [2, 3, 5, 8],
    "TREND": [True, False],
    "ZONE": [20, 30],
}
CURRENT = {"STOP_ATR": 1.5, "TARGET_R": 3.0, "MAX_HOURS": 48, "WINDOW": 3, "TREND": True, "ZONE": 30}
BOOKS = ["pionex", "pionex_majors", "funded"]
DATA = FEATS = TIMES = None
SPLIT = None  # "YYYY-MM-DD HH:MM" boundary between train and test


# ---------------- sharding (8 Nov: public hq-sims repo runs 20 GitHub machines at once) ----------------
# SHARD="i/n" -> only every n-th setting starting at i, saved as results/part_<suite>_<i>.json, no report.
# MERGE=1     -> no simulating: read every part file, then stress-test + write the report.
# OUT_TAG     -> suffix on report names (Oracle uses "_4y" so its long runs don't clash with the public repo's).
TAG = os.environ.get("OUT_TAG", "")


def compute(suite, combos, fn, workers):
    out = HERE / "results"
    if os.environ.get("MERGE"):
        rows = []
        for f in sorted(out.glob(f"part_{suite}_*.json")):
            rows += [tuple(x) for x in json.loads(f.read_text())]
        return rows, False
    shard = os.environ.get("SHARD")
    if shard:
        i, n = map(int, shard.split("/"))
        combos = combos[i::n]
    with Pool(workers) as pool:  # fork: workers share the loaded data
        rows = [(p, r) for p, r in pool.map(fn, combos, chunksize=4) if "error" not in r]
    if shard:
        (out / f"part_{suite}_{i}.json").write_text(json.dumps(rows))
        print(f"shard {shard}: {len(rows)} settings saved")
        return rows, True
    return rows, False


def load(days):
    """Binance 1h archive, cached per coin for 20h so reruns don't refetch."""
    CACHE.mkdir(exist_ok=True)
    data = {}
    for c in C.PAIRS:
        f = CACHE / f"sweep_{c}_{days}.json"
        if f.exists() and time.time() - f.stat().st_mtime < 72000:
            data[c] = json.loads(f.read_text())
        else:
            data[c] = C.bars_hist(c, days)
            f.write_text(json.dumps(data[c]))
    feats = {}
    for c, b in data.items():
        feats[c] = C.features(b)
        feats[c]["idx"] = {x["t"]: i for i, x in enumerate(b)}
    return data, feats


def metrics(name, bk):
    tr = bk["closed"]
    tr_a = [x for x in tr if x["close"] < SPLIT]
    tr_b = [x for x in tr if x["close"] >= SPLIT]
    months = {}
    for x in tr:
        months[x["close"][:7]] = months.get(x["close"][:7], 0) + x["pnl"]
    eq, peak, dd = C.BOOKS[name]["start"], C.BOOKS[name]["start"], 0.0
    for x in tr:
        eq += x["pnl"]
        peak = max(peak, eq)
        dd = max(dd, (peak - eq) / peak)
    m = {"trades": len(tr), "wins": round(sum(x["pnl"] > 0 for x in tr) / len(tr), 2) if tr else 0,
         "pnl": round(sum(x["pnl"] for x in tr), 2), "train": round(sum(x["pnl"] for x in tr_a), 2),
         "test": round(sum(x["pnl"] for x in tr_b), 2), "month_avg": round(sum(months.values()) / max(len(months), 1), 2),
         "month_worst": round(min(months.values()), 2) if months else 0,
         "months_up": f"{sum(v > 0 for v in months.values())}/{len(months)}", "max_dd": round(dd, 3)}
    if name == "funded":
        res = bk["results"]
        m["passes"] = sum(r["verdict"].startswith("PASS") for r in res)
        m["fails"] = sum(r["verdict"].startswith("FAIL") for r in res)
        m["test_passes"] = sum(r["verdict"].startswith("PASS") and r["end"] >= SPLIT[:10] for r in res)
    return m


def run(params, fee_mult=1.0):
    for k, v in params.items():
        setattr(C, k, v)
    C.FEE = 0.0005 * fee_mult
    books = {n: C.new_book(n) for n in BOOKS}
    events = []
    for t in TIMES:
        C.step(books, DATA, FEATS, t, [], events)
        events.clear()
    return {n: metrics(n, books[n]) for n in BOOKS}


def job(params):
    try:
        return params, run(params)
    except Exception as e:  # one bad combo must not kill the sweep
        return params, {"error": str(e)}


def passes(m, name):
    ok = m["train"] > 0 and m["test"] > 0
    if name == "funded":
        ok = ok and m["passes"] > m["fails"] / 2
    return ok


def score(m):
    return min(m["train"], m["test"] * 2)  # test is half the length of train


def label(p):
    return (f"stop {p['STOP_ATR']}ATR, target {p['TARGET_R']}R, time {p['MAX_HOURS']}h, window {p['WINDOW']}, "
            f"trend {'on' if p['TREND'] else 'off'}, zone {p['ZONE']}/{100 - p['ZONE']}")


def main(days=730, workers=2):
    global DATA, FEATS, TIMES, SPLIT
    t0 = time.time()
    DATA, FEATS = load(days)
    TIMES = C.all_times(DATA)
    SPLIT = datetime.fromtimestamp(TIMES[len(TIMES) * 2 // 3], timezone.utc).strftime("%Y-%m-%d %H:%M")
    combos = [dict(zip(GRID, v)) for v in itertools.product(*GRID.values())]
    rows, part_only = compute("confluence", combos, job, workers)
    if part_only:
        return
    # fee stress on each book's top 5 by score
    stress = {}
    for n in BOOKS:
        top = sorted(rows, key=lambda pr: score(pr[1][n]), reverse=True)[:5]
        for p, _ in top:
            key = json.dumps(p, sort_keys=True)
            if key not in stress:
                stress[key] = run(p, fee_mult=2.0)
    write(rows, stress, days, len(combos), time.time() - t0)


def write(rows, stress, days, n_combos, secs):
    out = HERE / "results"
    with open(out / f"sweep_confluence{TAG}.csv", "w", newline="") as f:
        w = csv.writer(f)
        cols = list(GRID)
        w.writerow(cols + [f"{n}_{k}" for n in BOOKS for k in ("pnl", "train", "test", "trades", "month_avg", "month_worst", "max_dd")]
                   + ["funded_passes", "funded_fails"])
        for p, r in rows:
            w.writerow([p[k] for k in cols] + [r[n][k] for n in BOOKS for k in ("pnl", "train", "test", "trades", "month_avg", "month_worst", "max_dd")]
                       + [r["funded"]["passes"], r["funded"]["fails"]])
    cur = next((r for p, r in rows if p == CURRENT), None)
    L = [f"# CONFLUENCE sweep: {n_combos} settings x 3 books, last {days} days of 1h bars",
         f"Updated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC on {os.environ.get('SIM_HOST', 'the Oracle server')} in {secs / 60:.0f} min. Paper maths only. "
         f"Train = before {SPLIT[:10]}, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).", ""]
    for n in BOOKS:
        cfg = C.BOOKS[n]
        cu = cfg["cur"]
        good = [(p, r) for p, r in rows if passes(r[n], n)]
        robust = [(p, r) for p, r in good
                  if stress.get(json.dumps(p, sort_keys=True), {}).get(n, {}).get("pnl", 1) > 0]
        ranked = sorted(good, key=lambda pr: score(pr[1][n]), reverse=True)[:8]
        L += [f"## {n} ({cu}{cfg['start']:.0f} start)",
              f"{len(good)} of {len(rows)} settings make money in both halves; {len(robust)} of the stress-tested top ones survive 2x fees."]
        if cur:
            c = cur[n]
            L.append(f"Current setting: P&L {cu}{c['pnl']:+.0f} (train {c['train']:+.0f}, test {c['test']:+.0f}), "
                     f"{c['trades']} trades, worst month {cu}{c['month_worst']:+.0f}"
                     + (f", {c['passes']} passes / {c['fails']} fails" if n == "funded" else ""))
        L += ["", "| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |"
              + (" pass/fail |" if n == "funded" else ""),
              "|---|---|---|---|---|---|---|---|---|---|---|" + ("---|" if n == "funded" else "")]
        for p, r in ranked:
            m = r[n]
            st = stress.get(json.dumps(p, sort_keys=True), {}).get(n)
            L.append(f"| {label(p)} | {m['pnl']:+.0f} | {m['train']:+.0f} | {m['test']:+.0f} | {m['trades']} | {m['wins']:.0%} | "
                     f"{m['month_avg']:+.0f} | {m['month_worst']:+.0f} | {m['months_up']} | {m['max_dd']:.0%} | "
                     f"{(f'{st['pnl']:+.0f}' if st else '-')} |" + (f" {m['passes']}/{m['fails']} |" if n == "funded" else ""))
        if not ranked:
            L.append("| none pass | | | | | | | | | | |")
        L.append("")
    L += ["Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). "
          "Nothing changes in the live paper bots until Lewis says yes."]
    (out / f"sweep_confluence{TAG}.md").write_text("\n".join(L))
    print("\n".join(L[:12]))


# ---------------- SMART suite ----------------
import smart as S

SGRID = {
    "BBSQ_STOP": [1.0, 1.5, 2.0, 2.5],
    "bbsq_target": [2.0, 3.0, 4.0, 6.0],
    "bbsq_max_h": [48, 120, 240],
    "SQ_BARS": [3, 6, 10],
    "MOVERS_PCT": [0.05, 0.08, 0.12],
    "trend_target": [1.5, 2.0, 3.0],
}
SCURRENT = {"BBSQ_STOP": 1.5, "bbsq_target": 3.0, "bbsq_max_h": 120, "SQ_BARS": 6, "MOVERS_PCT": 0.08, "trend_target": 2.0}
SBOOKS = [b for b in S.BOOKS if b.split("_")[0] in ("bbsq", "movers", "trend")]
SD = STIMES = None


def s_load(days):
    CACHE.mkdir(exist_ok=True)
    f = CACHE / f"sweep_smart_{days}.json"
    if f.exists() and time.time() - f.stat().st_mtime < 72000:
        raw = json.loads(f.read_text())
    else:
        d = S.load(days, days)
        raw = {"h1": d["h1"], "h4": d["h4"], "fund": {c: {str(k): v for k, v in fd.items()} for c, fd in d["fund"].items()}}
        f.write_text(json.dumps(raw))
    d = {"h1": raw["h1"], "h4": raw["h4"], "fund": {c: {int(k): v for k, v in fd.items()} for c, fd in raw["fund"].items()},
         "f4": {}, "i1": {}, "i4": {}}
    for c in d["h1"]:
        d["f4"][c] = S.feats4h(d["h4"][c])
        d["i1"][c] = {x["t"]: k for k, x in enumerate(d["h1"][c])}
        d["i4"][c] = {x["t"]: k for k, x in enumerate(d["h4"][c])}
    S.COINS = [c for c in S.COINS if c in d["h1"]]
    return d


def s_metrics(bk):
    tr = bk["closed"]
    months = {}
    for x in tr:
        months[x["close"][:7]] = months.get(x["close"][:7], 0) + x["pnl"]
    eq = peak = S.POT
    dd = 0.0
    for x in tr:
        eq += x["pnl"]; peak = max(peak, eq); dd = max(dd, (peak - eq) / peak)
    return {"trades": len(tr), "wins": round(sum(x["pnl"] > 0 for x in tr) / len(tr), 2) if tr else 0,
            "pnl": round(sum(x["pnl"] for x in tr), 2),
            "train": round(sum(x["pnl"] for x in tr if x["close"] < SPLIT), 2),
            "test": round(sum(x["pnl"] for x in tr if x["close"] >= SPLIT), 2),
            "month_avg": round(sum(months.values()) / max(len(months), 1), 2),
            "month_worst": round(min(months.values()), 2) if months else 0,
            "months_up": f"{sum(v > 0 for v in months.values())}/{len(months)}", "max_dd": round(dd, 3)}


def s_run(p, fee_mult=1.0):
    S.BBSQ_STOP, S.SQ_BARS, S.MOVERS_PCT = p["BBSQ_STOP"], p["SQ_BARS"], p["MOVERS_PCT"]
    S.STRATS["bbsq"]["target_r"], S.STRATS["bbsq"]["max_h"] = p["bbsq_target"], p["bbsq_max_h"]
    S.STRATS["trend"]["target_r"] = p["trend_target"]
    S.FEE = 0.0005 * fee_mult
    books = {n: S.new_book() for n in S.BOOKS}
    for t in STIMES:
        S.step(books, SD, t, [])
    return {n: s_metrics(books[n]) for n in SBOOKS}


def s_job(p):
    try:
        return p, s_run(p)
    except Exception as e:
        return p, {"error": str(e)}


def s_label(n, p):
    s = n.split("_")[0]
    if s == "bbsq":
        return f"stop {p['BBSQ_STOP']}ATR, target {p['bbsq_target']}R, time {p['bbsq_max_h']}h, squeeze {p['SQ_BARS']} bars"
    if s == "movers":
        return f"24h move {p['MOVERS_PCT']:.0%}"
    return f"target {p['trend_target']}R"


def s_key(n, p):  # settings that actually affect this book (the rest of the grid is noise for it)
    s = n.split("_")[0]
    keys = {"bbsq": ("BBSQ_STOP", "bbsq_target", "bbsq_max_h", "SQ_BARS"), "movers": ("MOVERS_PCT",), "trend": ("trend_target",)}[s]
    return tuple(p[k] for k in keys)


def main_smart(days=200, workers=2):
    global SD, STIMES, SPLIT
    t0 = time.time()
    SD = s_load(days)
    STIMES = sorted({x["t"] for b in SD["h1"].values() for x in b})
    SPLIT = datetime.fromtimestamp(STIMES[len(STIMES) * 2 // 3], timezone.utc).strftime("%Y-%m-%d %H:%M")
    combos = [dict(zip(SGRID, v)) for v in itertools.product(*SGRID.values())]
    rows, part_only = compute("smart", combos, s_job, workers)
    if part_only:
        return
    out = HERE / "results"
    with open(out / f"sweep_smart{TAG}.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(list(SGRID) + [f"{n}_{k}" for n in SBOOKS for k in ("pnl", "train", "test", "trades", "month_worst")])
        for p, r in rows:
            w.writerow([p[k] for k in SGRID] + [r[n][k] for n in SBOOKS for k in ("pnl", "train", "test", "trades", "month_worst")])
    cur = next((r for p, r in rows if p == SCURRENT), None)
    L = [f"# SMART sweep: {len(combos)} settings, last {days} days (Hyperliquid 1h/4h + real funding, £200 per book)",
         f"Updated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC on {os.environ.get('SIM_HOST', 'the Oracle server')} in {(time.time() - t0) / 60:.0f} min. Paper maths only. "
         f"Train = before {SPLIT[:10]}, test = after. '2x fees' = same setting with double fees.", ""]
    for n in SBOOKS:
        uniq = {}
        for p, r in rows:
            uniq.setdefault(s_key(n, p), (p, r))
        good = [(p, r) for p, r in uniq.values() if r[n]["train"] > 0 and r[n]["test"] > 0]
        ranked = sorted(good, key=lambda pr: score(pr[1][n]), reverse=True)[:6]
        L += [f"## {n}", f"{len(good)} of {len(uniq)} distinct settings make money in both halves."]
        if cur:
            c = cur[n]
            L.append(f"Current: P&L £{c['pnl']:+.0f} (train {c['train']:+.0f}, test {c['test']:+.0f}), {c['trades']} trades, worst month £{c['month_worst']:+.0f}")
        L += ["", "| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |", "|---|---|---|---|---|---|---|---|---|---|"]
        for p, r in ranked:
            m, st = r[n], s_run(p, 2.0)[n]
            L.append(f"| {s_label(n, p)} | {m['pnl']:+.0f} | {m['train']:+.0f} | {m['test']:+.0f} | {m['trades']} | {m['wins']:.0%} | "
                     f"{m['month_worst']:+.0f} | {m['months_up']} | {m['max_dd']:.0%} | {st['pnl']:+.0f} |")
        if not ranked:
            L.append("| none pass | | | | | | | | | |")
        L.append("")
    (out / f"sweep_smart{TAG}.md").write_text("\n".join(L))
    print("\n".join(L[:8]))


if __name__ == "__main__":
    a = sys.argv[1:]
    suite = a[0] if a and not a[0].isdigit() else "all"
    a = a[1:] if a and not a[0].isdigit() else a
    workers = int(a[1]) if len(a) > 1 else (os.cpu_count() or 2)
    if suite in ("confluence", "all"):
        main(int(a[0]) if a and suite == "confluence" else 730, workers)
    if suite in ("smart", "all"):
        main_smart(int(a[0]) if a and suite == "smart" else 200, workers)
