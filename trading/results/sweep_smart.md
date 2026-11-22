# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-22 19:58 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-17, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-18 (train -15, test -3), 123 trades, worst month £-59

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+6 (train +8, test -2), 114 trades, worst month £-11

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
50 of 144 distinct settings make money in both halves.
Current: P&L £+206 (train +172, test +34), 131 trades, worst month £-60

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +197 | +129 | +68 | 211 | 36% | -92 | 5/7 | 37% | +153 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +334 | +276 | +58 | 221 | 38% | -87 | 5/7 | 28% | +275 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +134 | +89 | +45 | 76 | 39% | -23 | 4/7 | 23% | +120 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +256 | +214 | +42 | 203 | 33% | -79 | 3/7 | 36% | +155 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +134 | +94 | +40 | 100 | 45% | -60 | 4/7 | 32% | +162 |
| stop 2.5ATR, target 2.0R, time 48h, squeeze 6 bars | +230 | +191 | +39 | 133 | 51% | -17 | 5/7 | 20% | +199 |

## bbsq_pro
47 of 144 distinct settings make money in both halves.
Current: P&L £+48 (train +42, test +6), 131 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +106 | +93 | +12 | 221 | 38% | -29 | 5/7 | 15% | +90 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +58 | +46 | +12 | 211 | 36% | -26 | 5/7 | 15% | +43 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +45 | +38 | +7 | 203 | 33% | -21 | 3/7 | 15% | +31 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +32 | +25 | +7 | 89 | 47% | -6 | 4/7 | 9% | +25 |
| stop 1.0ATR, target 6.0R, time 48h, squeeze 3 bars | +85 | +78 | +7 | 208 | 36% | -24 | 4/7 | 13% | +52 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +22 | +12 | +10 | 126 | 21% | -15 | 3/7 | 13% | +0 |

## movers_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £-2 (train +38, test -41), 366 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +219 | +207 | +13 | 596 | 40% | -25 | 4/7 | 27% | +77 |

## movers_pro
1 of 3 distinct settings make money in both halves.
Current: P&L £+9 (train +16, test -7), 365 trades, worst month £-18

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +37 | +37 | +0 | 595 | 40% | -5 | 4/7 | 13% | +18 |
