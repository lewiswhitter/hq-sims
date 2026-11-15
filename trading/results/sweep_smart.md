# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-15 21:10 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-10, test = after. '2x fees' = same setting with double fees.

## trend_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £+72 (train +125, test -53), 123 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| target 3.0R | +44 | +39 | +5 | 109 | 29% | -67 | 3/7 | 38% | +27 |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+7 (train +17, test -11), 114 trades, worst month £-11

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
26 of 144 distinct settings make money in both halves.
Current: P&L £+238 (train +232, test +6), 133 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +134 | +92 | +42 | 128 | 21% | -27 | 4/7 | 34% | +86 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +240 | +212 | +28 | 221 | 36% | -87 | 3/7 | 31% | +192 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +243 | +215 | +28 | 204 | 32% | -79 | 3/7 | 32% | +147 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +150 | +129 | +21 | 102 | 45% | -21 | 4/7 | 24% | +123 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +287 | +271 | +16 | 211 | 34% | -97 | 4/7 | 29% | +209 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +153 | +139 | +15 | 106 | 28% | -31 | 3/7 | 33% | +124 |

## bbsq_pro
14 of 144 distinct settings make money in both halves.
Current: P&L £+58 (train +57, test +1), 133 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +38 | +31 | +6 | 128 | 21% | -15 | 4/7 | 13% | +13 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +88 | +83 | +5 | 221 | 36% | -28 | 4/7 | 15% | +61 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +26 | +22 | +4 | 204 | 32% | -20 | 3/7 | 15% | +28 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +62 | +59 | +2 | 211 | 34% | -28 | 4/7 | 15% | +64 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +20 | +18 | +2 | 106 | 28% | -9 | 4/7 | 12% | -1 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 6 bars | +58 | +56 | +2 | 164 | 34% | -12 | 4/7 | 12% | +49 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+61 (train +134, test -73), 364 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+26 (train +39, test -13), 363 trades, worst month £-19

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
