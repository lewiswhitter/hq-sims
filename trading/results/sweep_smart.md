# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-20 07:38 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-14, test = after. '2x fees' = same setting with double fees.

## trend_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £+91 (train +114, test -23), 121 trades, worst month £-48

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| target 3.0R | +36 | +1 | +35 | 105 | 29% | -67 | 3/7 | 40% | +49 |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+20 (train +25, test -5), 112 trades, worst month £-12

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
21 of 144 distinct settings make money in both halves.
Current: P&L £+253 (train +252, test +1), 133 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +134 | +103 | +32 | 129 | 21% | -27 | 4/7 | 34% | +97 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +203 | +182 | +21 | 102 | 44% | -21 | 3/7 | 26% | +142 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 6 bars | +277 | +260 | +17 | 76 | 39% | -18 | 5/7 | 18% | +264 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +325 | +309 | +17 | 78 | 47% | -42 | 5/7 | 16% | +307 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +166 | +151 | +15 | 105 | 29% | -31 | 4/7 | 32% | +152 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +171 | +161 | +10 | 91 | 48% | -26 | 4/7 | 19% | +152 |

## bbsq_pro
9 of 144 distinct settings make money in both halves.
Current: P&L £+64 (train +64, test -0), 133 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +47 | +42 | +5 | 129 | 21% | -15 | 4/7 | 13% | +21 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 6 bars | +38 | +35 | +3 | 75 | 39% | -4 | 4/7 | 9% | +35 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 3 bars | +55 | +53 | +3 | 77 | 47% | -9 | 5/7 | 9% | +52 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +27 | +25 | +2 | 105 | 29% | -9 | 5/7 | 12% | +2 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 3 bars | +54 | +53 | +2 | 77 | 43% | -9 | 5/7 | 9% | +50 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +45 | +43 | +1 | 91 | 47% | -7 | 4/7 | 9% | +41 |

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
