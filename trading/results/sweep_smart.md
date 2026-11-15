# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-15 06:56 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-09, test = after. '2x fees' = same setting with double fees.

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
7 of 144 distinct settings make money in both halves.
Current: P&L £+232 (train +236, test -4), 135 trades, worst month £-40

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +262 | +244 | +18 | 223 | 36% | -87 | 4/8 | 29% | +214 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +297 | +279 | +18 | 206 | 32% | -79 | 4/8 | 30% | +188 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +104 | +93 | +11 | 104 | 44% | -40 | 4/8 | 27% | +66 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +25 | +15 | +10 | 129 | 20% | -40 | 3/8 | 42% | +5 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +86 | +80 | +6 | 213 | 34% | -92 | 3/8 | 42% | -3 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +109 | +104 | +5 | 108 | 28% | -40 | 4/8 | 37% | +94 |

## bbsq_pro
6 of 144 distinct settings make money in both halves.
Current: P&L £+49 (train +50, test -1), 135 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +79 | +76 | +3 | 223 | 36% | -27 | 5/8 | 15% | +74 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +35 | +32 | +3 | 206 | 32% | -20 | 4/8 | 15% | +22 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +11 | +10 | +1 | 108 | 28% | -8 | 4/8 | 12% | -10 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +57 | +56 | +0 | 213 | 34% | -27 | 4/8 | 15% | +57 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +28 | +28 | +0 | 129 | 20% | -11 | 4/8 | 12% | +3 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 6 bars | +65 | +65 | +0 | 166 | 34% | -12 | 5/8 | 12% | +50 |

## movers_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £-7 (train +62, test -68), 364 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +452 | +439 | +13 | 588 | 41% | -25 | 5/7 | 21% | +318 |

## movers_pro
1 of 3 distinct settings make money in both halves.
Current: P&L £+35 (train +48, test -13), 363 trades, worst month £-20

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +91 | +90 | +0 | 587 | 41% | -6 | 5/7 | 13% | +65 |
