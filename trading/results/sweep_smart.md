# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-22 07:15 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-16, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-12 (train -3, test -8), 119 trades, worst month £-59

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+4 (train +6, test -2), 110 trades, worst month £-11

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
69 of 144 distinct settings make money in both halves.
Current: P&L £+264 (train +230, test +34), 132 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +323 | +254 | +68 | 212 | 36% | -97 | 5/7 | 30% | +185 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +373 | +319 | +54 | 221 | 38% | -97 | 5/7 | 27% | +319 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +164 | +99 | +66 | 127 | 21% | -27 | 4/7 | 33% | +130 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 3 bars | +195 | +148 | +47 | 116 | 31% | -31 | 4/7 | 30% | +111 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +173 | +133 | +40 | 101 | 46% | -22 | 4/7 | 27% | +134 |
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +238 | +198 | +40 | 75 | 33% | -16 | 6/7 | 22% | +219 |

## bbsq_pro
50 of 144 distinct settings make money in both halves.
Current: P&L £+59 (train +53, test +6), 132 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +72 | +60 | +13 | 212 | 36% | -28 | 5/7 | 15% | +75 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +119 | +107 | +12 | 221 | 38% | -30 | 5/7 | 15% | +86 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +41 | +30 | +11 | 127 | 21% | -15 | 4/7 | 13% | +16 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +39 | +32 | +7 | 90 | 48% | -6 | 4/7 | 9% | +33 |
| stop 1.0ATR, target 6.0R, time 48h, squeeze 3 bars | +89 | +81 | +7 | 208 | 36% | -24 | 4/7 | 13% | +90 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +41 | +35 | +6 | 204 | 33% | -20 | 3/7 | 15% | +28 |

## movers_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £-2 (train +40, test -42), 366 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +217 | +211 | +6 | 595 | 40% | -25 | 4/7 | 27% | +75 |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+9 (train +16, test -7), 365 trades, worst month £-18

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
