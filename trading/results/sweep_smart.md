# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-14 22:42 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-09, test = after. '2x fees' = same setting with double fees.

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
8 of 144 distinct settings make money in both halves.
Current: P&L £+221 (train +225, test -4), 135 trades, worst month £-33

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +261 | +243 | +18 | 223 | 36% | -87 | 4/8 | 29% | +212 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +296 | +278 | +18 | 206 | 32% | -79 | 4/8 | 30% | +186 |
| stop 2.0ATR, target 2.0R, time 240h, squeeze 6 bars | +156 | +145 | +11 | 104 | 45% | -27 | 5/8 | 26% | +115 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +141 | +131 | +10 | 129 | 21% | -40 | 4/8 | 32% | +92 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +257 | +251 | +6 | 213 | 34% | -97 | 5/8 | 30% | +81 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +180 | +175 | +5 | 108 | 29% | -31 | 4/8 | 31% | +150 |

## bbsq_pro
7 of 144 distinct settings make money in both halves.
Current: P&L £+64 (train +66, test -1), 135 trades, worst month £-9

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 3.0R, time 48h, squeeze 3 bars | +96 | +93 | +3 | 223 | 36% | -29 | 5/8 | 15% | +74 |
| stop 1.0ATR, target 3.0R, time 120h, squeeze 3 bars | +49 | +46 | +3 | 206 | 32% | -22 | 4/8 | 15% | +21 |
| stop 1.5ATR, target 4.0R, time 240h, squeeze 6 bars | +29 | +28 | +1 | 108 | 29% | -9 | 5/8 | 12% | +3 |
| stop 1.0ATR, target 4.0R, time 48h, squeeze 3 bars | +74 | +73 | +0 | 213 | 34% | -29 | 5/8 | 15% | +55 |
| stop 2.0ATR, target 3.0R, time 240h, squeeze 6 bars | +15 | +15 | +0 | 92 | 33% | -5 | 4/8 | 9% | +12 |
| stop 1.0ATR, target 6.0R, time 240h, squeeze 6 bars | +51 | +50 | +0 | 129 | 21% | -12 | 5/8 | 12% | +22 |

## movers_lewis
1 of 3 distinct settings make money in both halves.
Current: P&L £+3 (train +62, test -58), 362 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +457 | +439 | +18 | 587 | 41% | -25 | 5/7 | 21% | +323 |

## movers_pro
1 of 3 distinct settings make money in both halves.
Current: P&L £+36 (train +48, test -11), 361 trades, worst month £-20

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| 24h move 5% | +92 | +90 | +1 | 586 | 41% | -6 | 5/7 | 13% | +66 |
