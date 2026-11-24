# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-24 22:44 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-19, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-97 (train -69, test -28), 119 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-6 (train -6, test +0), 111 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
45 of 144 distinct settings make money in both halves.
Current: P&L £+269 (train +234, test +34), 129 trades, worst month £-30

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +218 | +163 | +55 | 98 | 46% | -21 | 3/7 | 22% | +171 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +156 | +114 | +42 | 125 | 21% | -40 | 3/7 | 34% | +112 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +131 | +81 | +50 | 74 | 39% | -25 | 4/7 | 23% | +119 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +125 | +87 | +38 | 76 | 46% | -34 | 4/7 | 26% | +119 |
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +269 | +234 | +34 | 129 | 42% | -30 | 4/7 | 24% | +244 |
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +109 | +67 | +42 | 75 | 33% | -16 | 4/7 | 29% | +128 |

## bbsq_pro
41 of 144 distinct settings make money in both halves.
Current: P&L £+74 (train +68, test +7), 129 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +35 | +25 | +10 | 89 | 47% | -6 | 4/7 | 9% | +27 |
| stop 2.5ATR, target 3.0R, time 120h, squeeze 3 bars | +75 | +67 | +8 | 121 | 52% | -23 | 6/7 | 8% | +49 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +45 | +38 | +7 | 98 | 46% | -7 | 3/7 | 10% | +47 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +39 | +33 | +7 | 125 | 21% | -15 | 3/7 | 13% | +33 |
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +74 | +68 | +7 | 129 | 42% | -9 | 2/7 | 11% | +67 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +36 | +30 | +6 | 75 | 45% | -8 | 5/7 | 9% | +32 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+48 (train +170, test -122), 369 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+7 (train +27, test -20), 368 trades, worst month £-18

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
