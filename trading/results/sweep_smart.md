# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-24 10:15 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-18, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-38 (train -45, test +7), 122 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-3 (train -3, test +0), 113 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
46 of 144 distinct settings make money in both halves.
Current: P&L £+259 (train +224, test +34), 130 trades, worst month £-40

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +148 | +95 | +52 | 76 | 33% | -21 | 5/7 | 29% | +112 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +130 | +80 | +50 | 99 | 45% | -40 | 3/7 | 27% | +69 |
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +259 | +224 | +34 | 130 | 42% | -40 | 4/7 | 24% | +180 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +114 | +80 | +34 | 103 | 28% | -36 | 3/7 | 38% | +102 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 3 bars | +123 | +66 | +57 | 114 | 31% | -52 | 3/7 | 38% | +42 |
| stop 2.5ATR, target 2.0R, time 48h, squeeze 6 bars | +233 | +202 | +31 | 132 | 52% | -17 | 5/7 | 20% | +204 |

## bbsq_pro
45 of 144 distinct settings make money in both halves.
Current: P&L £+48 (train +42, test +6), 130 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +33 | +23 | +10 | 126 | 21% | -13 | 3/7 | 12% | +18 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +27 | +18 | +9 | 89 | 46% | -6 | 3/7 | 9% | +14 |
| stop 2.5ATR, target 3.0R, time 120h, squeeze 3 bars | +58 | +52 | +6 | 120 | 51% | -22 | 5/7 | 8% | +33 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +41 | +35 | +6 | 74 | 38% | -10 | 4/7 | 9% | +32 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +28 | +22 | +6 | 75 | 44% | -8 | 5/7 | 9% | +24 |
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +48 | +42 | +6 | 130 | 42% | -9 | 2/7 | 11% | +40 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+48 (train +165, test -116), 369 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+7 (train +27, test -19), 368 trades, worst month £-18

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
