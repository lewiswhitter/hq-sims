# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-15 12:08 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-09, test = after. '2x fees' = same setting with double fees.

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
14 of 144 distinct settings make money in both halves.
Current: P&L £+238 (train +237, test +1), 133 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +240 | +212 | +28 | 221 | 36% | -87 | 3/7 | 31% | +192 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +243 | +215 | +28 | 204 | 32% | -79 | 3/7 | 32% | +147 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +112 | +92 | +20 | 127 | 20% | -27 | 4/7 | 34% | +64 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +287 | +271 | +16 | 211 | 34% | -97 | 4/7 | 29% | +209 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 6 bars | +174 | +161 | +13 | 164 | 34% | -65 | 5/7 | 24% | +287 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +150 | +139 | +11 | 102 | 45% | -21 | 4/7 | 24% | +123 |

## bbsq_pro
12 of 144 distinct settings make money in both halves.
Current: P&L £+58 (train +58, test -0), 133 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +88 | +83 | +5 | 221 | 36% | -28 | 4/7 | 15% | +61 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +26 | +22 | +4 | 204 | 32% | -20 | 3/7 | 15% | +28 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +34 | +31 | +3 | 127 | 20% | -15 | 4/7 | 13% | +9 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +62 | +59 | +2 | 211 | 34% | -28 | 4/7 | 15% | +64 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 6 bars | +58 | +56 | +2 | 164 | 34% | -12 | 4/7 | 12% | +49 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +20 | +19 | +1 | 106 | 28% | -9 | 4/7 | 12% | -1 |

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
