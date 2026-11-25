# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-25 09:00 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-19, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-28 (train -34, test +7), 119 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-0 (train -0, test +0), 110 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
50 of 144 distinct settings make money in both halves.
Current: P&L £+237 (train +202, test +34), 128 trades, worst month £-45

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +243 | +188 | +55 | 97 | 46% | -21 | 3/7 | 21% | +106 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +180 | +129 | +50 | 88 | 49% | -26 | 4/7 | 20% | +157 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +151 | +104 | +47 | 124 | 21% | -35 | 3/7 | 34% | +117 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +259 | +216 | +43 | 75 | 47% | -34 | 5/7 | 20% | +244 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 3 bars | +223 | +185 | +38 | 112 | 32% | -31 | 4/7 | 28% | +193 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 3 bars | +197 | +160 | +37 | 74 | 45% | -34 | 5/7 | 23% | +183 |

## bbsq_pro
43 of 144 distinct settings make money in both halves.
Current: P&L £+78 (train +72, test +7), 128 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +37 | +25 | +12 | 88 | 48% | -6 | 4/7 | 9% | +31 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +56 | +47 | +9 | 72 | 39% | -9 | 5/7 | 8% | +52 |
| stop 2.5ATR, target 3.0R, time 120h, squeeze 3 bars | +78 | +70 | +8 | 120 | 53% | -22 | 6/7 | 8% | +52 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +38 | +30 | +8 | 74 | 46% | -8 | 5/7 | 9% | +35 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +48 | +41 | +7 | 97 | 46% | -7 | 3/7 | 10% | +51 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 3 bars | +39 | +32 | +7 | 73 | 44% | -8 | 5/7 | 9% | +36 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+44 (train +166, test -122), 369 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+8 (train +28, test -20), 368 trades, worst month £-18

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
