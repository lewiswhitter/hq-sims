# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-24 00:12 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-18, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-53 (train -55, test +2), 123 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-5 (train -5, test -1), 114 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
49 of 144 distinct settings make money in both halves.
Current: P&L £+259 (train +210, test +49), 130 trades, worst month £-40

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +259 | +210 | +49 | 130 | 42% | -40 | 4/7 | 24% | +180 |
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +148 | +100 | +47 | 76 | 33% | -21 | 5/7 | 29% | +112 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +205 | +159 | +46 | 210 | 36% | -97 | 5/7 | 37% | +127 |
| stop 2.5ATR, target 2.0R, time 48h, squeeze 6 bars | +233 | +192 | +41 | 132 | 52% | -17 | 5/7 | 20% | +204 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +130 | +90 | +40 | 99 | 45% | -40 | 3/7 | 27% | +69 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 3 bars | +123 | +71 | +52 | 114 | 31% | -52 | 3/7 | 38% | +42 |

## bbsq_pro
45 of 144 distinct settings make money in both halves.
Current: P&L £+48 (train +40, test +8), 130 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +33 | +24 | +9 | 126 | 21% | -13 | 3/7 | 12% | +18 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +27 | +19 | +9 | 89 | 46% | -6 | 3/7 | 9% | +14 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +81 | +72 | +9 | 210 | 36% | -29 | 5/7 | 15% | +45 |
| stop 1.5ATR, target 3.0R, time 120h, squeeze 6 bars | +48 | +40 | +8 | 130 | 42% | -9 | 2/7 | 11% | +40 |
| stop 1.0ATR, target 4.0R, time 240h, squeeze 6 bars | +55 | +48 | +8 | 141 | 27% | -13 | 2/7 | 14% | +40 |
| stop 1.0ATR, target 6.0R, time 48h, squeeze 3 bars | +87 | +81 | +6 | 207 | 36% | -24 | 4/7 | 13% | +71 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-106 (train -106, test +0), 143 trades, worst month £-62

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-13 (train +4, test -17), 371 trades, worst month £-16

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
