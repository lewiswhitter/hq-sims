# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-21 21:09 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-16, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+104 (train +112, test -8), 120 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+17 (train +20, test -2), 111 trades, worst month £-11

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
61 of 144 distinct settings make money in both halves.
Current: P&L £+325 (train +292, test +34), 134 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +334 | +266 | +68 | 214 | 36% | -97 | 5/7 | 29% | +302 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +415 | +349 | +66 | 128 | 23% | -43 | 4/7 | 20% | +358 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +435 | +381 | +54 | 223 | 39% | -97 | 5/7 | 25% | +356 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 3 bars | +415 | +368 | +47 | 117 | 32% | -31 | 4/7 | 19% | +318 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 6 bars | +198 | +155 | +43 | 92 | 45% | -29 | 3/7 | 23% | +184 |
| stop 2.0ATR, target 3.0R, time 240h, squeeze 6 bars | +135 | +93 | +42 | 90 | 34% | -20 | 2/7 | 29% | +152 |

## bbsq_pro
49 of 144 distinct settings make money in both halves.
Current: P&L £+80 (train +74, test +6), 134 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +109 | +94 | +14 | 214 | 36% | -31 | 5/7 | 15% | +68 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +92 | +79 | +13 | 128 | 23% | -18 | 4/7 | 13% | +81 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +113 | +101 | +12 | 223 | 39% | -29 | 5/7 | 15% | +96 |
| stop 1.0ATR, target 6.0R, time 48h, squeeze 3 bars | +96 | +89 | +7 | 210 | 37% | -25 | 4/7 | 13% | +78 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +36 | +28 | +7 | 92 | 48% | -6 | 4/7 | 9% | +29 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 6 bars | +41 | +34 | +7 | 76 | 39% | -4 | 4/7 | 9% | +40 |

## movers_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £-2 (train +45, test -48), 366 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +217 | +211 | +6 | 595 | 40% | -25 | 4/7 | 27% | +75 |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+9 (train +17, test -8), 365 trades, worst month £-18

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
