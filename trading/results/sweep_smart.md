# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-15 11:38 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-09, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-52 (train +0, test -53), 125 trades, worst month £-59

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+2 (train +12, test -10), 116 trades, worst month £-11

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
11 of 144 distinct settings make money in both halves.
Current: P&L £+187 (train +186, test +1), 134 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +234 | +206 | +28 | 222 | 36% | -87 | 3/8 | 36% | +55 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +237 | +209 | +28 | 205 | 32% | -79 | 3/8 | 33% | +136 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 6 bars | +110 | +88 | +23 | 165 | 34% | -65 | 5/8 | 32% | +55 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +55 | +35 | +20 | 128 | 20% | -30 | 4/8 | 38% | +20 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +138 | +122 | +16 | 212 | 34% | -92 | 4/8 | 37% | +86 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +118 | +107 | +11 | 103 | 45% | -27 | 4/8 | 30% | +145 |

## bbsq_pro
12 of 144 distinct settings make money in both halves.
Current: P&L £+54 (train +54, test -0), 134 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +84 | +79 | +5 | 222 | 36% | -27 | 4/8 | 15% | +63 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +26 | +21 | +4 | 205 | 32% | -20 | 3/8 | 15% | +13 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +30 | +28 | +3 | 128 | 20% | -14 | 4/8 | 13% | +6 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +80 | +77 | +3 | 212 | 34% | -30 | 4/8 | 15% | +60 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 6 bars | +49 | +47 | +2 | 165 | 34% | -11 | 4/8 | 12% | +45 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +16 | +15 | +1 | 107 | 28% | -9 | 4/8 | 12% | -7 |

## movers_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £-12 (train +62, test -73), 365 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +447 | +439 | +8 | 589 | 41% | -25 | 5/7 | 21% | +313 |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+34 (train +48, test -14), 364 trades, worst month £-20

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
