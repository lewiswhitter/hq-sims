# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-26 21:52 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-21, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-14 (train -16, test +2), 118 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+6 (train +6, test -1), 109 trades, worst month £-11

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
38 of 144 distinct settings make money in both halves.
Current: P&L £+232 (train +202, test +29), 129 trades, worst month £-45

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +180 | +129 | +50 | 88 | 49% | -26 | 4/7 | 20% | +157 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +233 | +188 | +45 | 98 | 46% | -21 | 3/7 | 21% | +101 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +259 | +216 | +43 | 75 | 47% | -34 | 5/7 | 20% | +244 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +146 | +104 | +42 | 125 | 21% | -35 | 3/7 | 34% | +112 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 3 bars | +197 | +160 | +37 | 74 | 45% | -34 | 5/7 | 23% | +183 |
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +232 | +202 | +29 | 129 | 42% | -45 | 4/7 | 25% | +143 |

## bbsq_pro
37 of 144 distinct settings make money in both halves.
Current: P&L £+77 (train +72, test +6), 129 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +37 | +25 | +12 | 88 | 48% | -6 | 4/7 | 9% | +31 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +56 | +45 | +11 | 72 | 39% | -9 | 5/7 | 8% | +52 |
| stop 2.5ATR, target 3.0R, time 120h, squeeze 3 bars | +78 | +70 | +8 | 120 | 53% | -22 | 6/7 | 8% | +52 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +38 | +30 | +8 | 74 | 46% | -8 | 5/7 | 9% | +35 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 3 bars | +39 | +32 | +7 | 73 | 44% | -8 | 5/7 | 9% | +36 |
| stop 2.5ATR, target 6.0R, time 240h, squeeze 6 bars | +21 | +13 | +9 | 70 | 33% | -7 | 4/7 | 8% | +20 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-100 (train -100, test +0), 133 trades, worst month £-55

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-0 (train +19, test -19), 369 trades, worst month £-17

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
