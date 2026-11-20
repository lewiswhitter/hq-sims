# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-20 20:41 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-15, test = after. '2x fees' = same setting with double fees.

## trend_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £+90 (train +113, test -23), 121 trades, worst month £-48

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| target 3.0R | +66 | +31 | +35 | 106 | 29% | -67 | 3/7 | 36% | +76 |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+20 (train +24, test -5), 112 trades, worst month £-12

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
38 of 144 distinct settings make money in both halves.
Current: P&L £+292 (train +302, test -10), 131 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +347 | +296 | +51 | 203 | 33% | -79 | 3/7 | 29% | +210 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +280 | +236 | +44 | 221 | 37% | -87 | 4/7 | 32% | +202 |
| stop 2.0ATR, target 4.0R, time 240h, squeeze 6 bars | +190 | +150 | +40 | 81 | 35% | -25 | 5/7 | 24% | +144 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +251 | +211 | +40 | 102 | 45% | -21 | 4/7 | 20% | +193 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +179 | +140 | +39 | 212 | 35% | -92 | 3/7 | 37% | +34 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +213 | +176 | +37 | 128 | 21% | -38 | 4/7 | 28% | +181 |

## bbsq_pro
28 of 144 distinct settings make money in both halves.
Current: P&L £+41 (train +43, test -2), 131 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +97 | +89 | +9 | 221 | 37% | -28 | 5/7 | 15% | +67 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +47 | +38 | +9 | 203 | 33% | -21 | 3/7 | 15% | +21 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +69 | +62 | +7 | 212 | 35% | -28 | 4/7 | 15% | +52 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 6 bars | +62 | +55 | +6 | 166 | 35% | -11 | 4/7 | 12% | +53 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +51 | +45 | +6 | 128 | 21% | -16 | 4/7 | 13% | +25 |
| stop 1.0ATR, target 3.0R, time 240h, squeeze 3 bars | +79 | +74 | +6 | 191 | 31% | -29 | 3/7 | 19% | +63 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+62 (train +132, test -70), 363 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+10 (train +21, test -12), 362 trades, worst month £-18

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
