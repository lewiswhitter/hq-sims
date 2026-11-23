# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-23 08:02 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-17, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-53 (train -50, test -3), 123 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-5 (train -4, test -1), 114 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
55 of 144 distinct settings make money in both halves.
Current: P&L £+206 (train +167, test +39), 131 trades, worst month £-60

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +197 | +131 | +66 | 211 | 36% | -92 | 5/7 | 37% | +153 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +334 | +274 | +60 | 221 | 38% | -87 | 5/7 | 28% | +275 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +256 | +209 | +47 | 203 | 33% | -79 | 3/7 | 36% | +155 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +134 | +89 | +45 | 76 | 39% | -23 | 4/7 | 23% | +120 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +134 | +94 | +40 | 100 | 45% | -60 | 4/7 | 32% | +162 |
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +206 | +167 | +39 | 131 | 41% | -60 | 4/7 | 32% | +183 |

## bbsq_pro
52 of 144 distinct settings make money in both halves.
Current: P&L £+48 (train +41, test +7), 131 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +106 | +93 | +13 | 221 | 38% | -29 | 5/7 | 15% | +90 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +58 | +46 | +12 | 211 | 36% | -26 | 5/7 | 15% | +43 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +45 | +37 | +8 | 203 | 33% | -21 | 3/7 | 15% | +31 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +32 | +25 | +7 | 89 | 47% | -6 | 4/7 | 9% | +25 |
| stop 1.0ATR, target 4.0R, time 240h, squeeze 6 bars | +37 | +30 | +7 | 142 | 27% | -15 | 2/7 | 14% | +32 |
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +48 | +41 | +7 | 131 | 41% | -9 | 2/7 | 11% | +42 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-8 (train +53, test -61), 368 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+8 (train +18, test -10), 367 trades, worst month £-18

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
