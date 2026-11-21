# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-21 19:37 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-16, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+104 (train +112, test -8), 120 trades, worst month £-44

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+17 (train +20, test -2), 111 trades, worst month £-11

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
61 of 144 distinct settings make money in both halves.
Current: P&L £+408 (train +374, test +34), 133 trades, worst month £-25

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +354 | +285 | +68 | 214 | 36% | -97 | 5/7 | 28% | +282 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +343 | +277 | +66 | 127 | 22% | -27 | 4/7 | 23% | +286 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +439 | +385 | +54 | 223 | 39% | -97 | 5/7 | 25% | +359 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 3 bars | +225 | +177 | +47 | 115 | 32% | -31 | 4/7 | 28% | +191 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 6 bars | +198 | +155 | +43 | 92 | 45% | -29 | 3/7 | 23% | +184 |
| stop 2.0ATR, target 4.0R, time 240h, squeeze 6 bars | +140 | +100 | +40 | 80 | 35% | -25 | 4/7 | 24% | +121 |

## bbsq_pro
50 of 144 distinct settings make money in both halves.
Current: P&L £+101 (train +94, test +7), 133 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +101 | +87 | +14 | 214 | 36% | -31 | 5/7 | 15% | +81 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +71 | +59 | +12 | 127 | 22% | -16 | 4/7 | 13% | +63 |
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +113 | +102 | +12 | 223 | 39% | -29 | 5/7 | 15% | +96 |
| stop 1.0ATR, target 6.0R, time 48h, squeeze 3 bars | +117 | +109 | +8 | 210 | 37% | -27 | 4/7 | 13% | +78 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +105 | +98 | +8 | 206 | 34% | -26 | 4/7 | 15% | +70 |
| stop 2.5ATR, target 2.0R, time 240h, squeeze 3 bars | +51 | +43 | +8 | 92 | 49% | -7 | 4/7 | 9% | +43 |

## movers_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £+49 (train +91, test -42), 366 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +184 | +173 | +11 | 595 | 40% | -25 | 4/7 | 29% | +15 |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+7 (train +14, test -7), 365 trades, worst month £-17

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
