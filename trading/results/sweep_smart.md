# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-27 21:35 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-22, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-14 (train -7, test -8), 118 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+6 (train +8, test -2), 109 trades, worst month £-11

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
37 of 144 distinct settings make money in both halves.
Current: P&L £+232 (train +202, test +29), 129 trades, worst month £-45

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +185 | +134 | +50 | 87 | 49% | -26 | 4/7 | 20% | +168 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +233 | +188 | +45 | 98 | 46% | -21 | 3/7 | 21% | +101 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +264 | +221 | +43 | 74 | 47% | -34 | 5/7 | 19% | +249 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +146 | +104 | +42 | 125 | 21% | -35 | 3/7 | 34% | +112 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 3 bars | +202 | +165 | +37 | 73 | 45% | -34 | 5/7 | 22% | +188 |
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +232 | +202 | +29 | 129 | 42% | -45 | 4/7 | 25% | +143 |

## bbsq_pro
36 of 144 distinct settings make money in both halves.
Current: P&L £+77 (train +72, test +6), 129 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +40 | +29 | +12 | 87 | 48% | -6 | 4/7 | 9% | +34 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +56 | +45 | +11 | 72 | 39% | -9 | 5/7 | 8% | +52 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +42 | +33 | +8 | 73 | 47% | -8 | 5/7 | 9% | +39 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 3 bars | +43 | +36 | +7 | 72 | 44% | -8 | 5/7 | 9% | +40 |
| stop 2.5ATR, target 6.0R, time 240h, squeeze 6 bars | +21 | +13 | +9 | 70 | 33% | -7 | 4/7 | 8% | +20 |
| stop 2.5ATR, target 3.0R, time 120h, squeeze 3 bars | +79 | +73 | +6 | 120 | 53% | -23 | 6/7 | 8% | +54 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+59 (train +175, test -115), 369 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+11 (train +30, test -19), 368 trades, worst month £-18

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
