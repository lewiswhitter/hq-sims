# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-19 07:46 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-13, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+185 (train +211, test -26), 125 trades, worst month £-59

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+36 (train +41, test -6), 116 trades, worst month £-12

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
24 of 144 distinct settings make money in both halves.
Current: P&L £+233 (train +232, test +1), 134 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +129 | +92 | +37 | 129 | 21% | -27 | 4/7 | 34% | +81 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +243 | +215 | +28 | 204 | 32% | -79 | 3/7 | 32% | +147 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +150 | +129 | +21 | 102 | 45% | -21 | 4/7 | 24% | +123 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +235 | +216 | +20 | 90 | 49% | -27 | 4/7 | 17% | +206 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +311 | +295 | +17 | 78 | 47% | -42 | 5/7 | 17% | +301 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +153 | +139 | +15 | 106 | 28% | -31 | 3/7 | 33% | +124 |

## bbsq_pro
13 of 144 distinct settings make money in both halves.
Current: P&L £+57 (train +57, test -0), 134 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +37 | +31 | +6 | 129 | 21% | -15 | 4/7 | 13% | +12 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +26 | +22 | +4 | 204 | 32% | -20 | 3/7 | 15% | +28 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +56 | +53 | +3 | 77 | 47% | -9 | 5/7 | 9% | +52 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +20 | +18 | +2 | 106 | 28% | -9 | 4/7 | 12% | -1 |
| stop 2.0ATR, target 3.0R, time 240h, squeeze 6 bars | +9 | +7 | +2 | 90 | 32% | -5 | 3/7 | 9% | +6 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 3 bars | +46 | +45 | +2 | 77 | 43% | -9 | 5/7 | 9% | +42 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+113 (train +193, test -80), 365 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+27 (train +42, test -15), 364 trades, worst month £-19

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
