# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-17 19:08 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-12, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+185 (train +216, test -31), 125 trades, worst month £-59

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+36 (train +42, test -7), 116 trades, worst month £-12

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
26 of 144 distinct settings make money in both halves.
Current: P&L £+233 (train +232, test +1), 134 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +134 | +92 | +42 | 128 | 21% | -27 | 4/7 | 34% | +86 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +243 | +215 | +28 | 204 | 32% | -79 | 3/7 | 32% | +147 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +150 | +129 | +21 | 102 | 45% | -21 | 4/7 | 24% | +123 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +235 | +216 | +20 | 90 | 49% | -27 | 4/7 | 17% | +206 |
| stop 2.5ATR, target 3.0R, time 120h, squeeze 3 bars | +322 | +305 | +17 | 122 | 52% | -66 | 5/7 | 14% | +276 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +311 | +295 | +17 | 78 | 47% | -42 | 5/7 | 17% | +301 |

## bbsq_pro
14 of 144 distinct settings make money in both halves.
Current: P&L £+57 (train +57, test -0), 134 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +38 | +31 | +6 | 128 | 21% | -15 | 4/7 | 13% | +13 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +26 | +22 | +4 | 204 | 32% | -20 | 3/7 | 15% | +28 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +56 | +53 | +3 | 77 | 47% | -9 | 5/7 | 9% | +52 |
| stop 2.5ATR, target 3.0R, time 120h, squeeze 3 bars | +89 | +86 | +3 | 121 | 52% | -24 | 6/7 | 8% | +62 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +20 | +18 | +2 | 106 | 28% | -9 | 4/7 | 12% | -1 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 6 bars | +58 | +56 | +2 | 164 | 34% | -12 | 4/7 | 12% | +49 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+92 (train +165, test -73), 364 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+25 (train +38, test -13), 363 trades, worst month £-19

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
