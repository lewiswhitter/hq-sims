# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-21 07:34 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-15, test = after. '2x fees' = same setting with double fees.

## trend_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £+213 (train +226, test -13), 122 trades, worst month £-59

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| target 3.0R | +78 | +43 | +35 | 104 | 30% | -67 | 3/7 | 34% | +71 |

## trend_pro
1 of 3 distinct settings make money in both halves.
Current: P&L £+29 (train +32, test -3), 113 trades, worst month £-12

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| target 3.0R | +8 | +4 | +4 | 100 | 31% | -15 | 3/7 | 10% | +6 |

## bbsq_lewis
66 of 144 distinct settings make money in both halves.
Current: P&L £+336 (train +302, test +34), 134 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +368 | +300 | +68 | 213 | 36% | -97 | 5/7 | 28% | +271 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +486 | +419 | +68 | 223 | 39% | -97 | 5/7 | 24% | +361 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +242 | +176 | +66 | 129 | 22% | -38 | 4/7 | 28% | +209 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +407 | +351 | +56 | 205 | 34% | -59 | 4/7 | 25% | +335 |
| stop 1.0ATR, target 4.0R, time 240h, squeeze 6 bars | +333 | +280 | +53 | 145 | 28% | -69 | 4/7 | 26% | +277 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +261 | +211 | +50 | 103 | 46% | -21 | 4/7 | 20% | +202 |

## bbsq_pro
53 of 144 distinct settings make money in both halves.
Current: P&L £+48 (train +43, test +6), 134 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +142 | +126 | +16 | 223 | 39% | -32 | 5/7 | 15% | +105 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +84 | +71 | +13 | 213 | 36% | -29 | 5/7 | 15% | +66 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +57 | +45 | +11 | 129 | 22% | -16 | 4/7 | 13% | +30 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +82 | +71 | +11 | 205 | 34% | -24 | 4/7 | 15% | +47 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +45 | +35 | +10 | 91 | 48% | -7 | 4/7 | 9% | +38 |
| stop 1.0ATR, target 4.0R, time 240h, squeeze 6 bars | +63 | +53 | +10 | 145 | 28% | -13 | 3/7 | 14% | +57 |

## movers_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £+57 (train +89, test -32), 366 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +191 | +175 | +16 | 595 | 40% | -25 | 4/7 | 29% | +44 |

## movers_pro
1 of 3 distinct settings make money in both halves.
Current: P&L £+8 (train +13, test -6), 365 trades, worst month £-17

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +36 | +35 | +1 | 594 | 40% | -5 | 4/7 | 13% | +16 |
