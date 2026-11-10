# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-10 19:59 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-05, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-109 (train -39, test -70), 105 trades, worst month £-55

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-21 (train -10, test -12), 117 trades, worst month £-12

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
3 of 144 distinct settings make money in both halves.
Current: P&L £+209 (train +227, test -18), 134 trades, worst month £-65

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +105 | +69 | +36 | 78 | 31% | -65 | 6/8 | 40% | +96 |
| stop 2.5ATR, target 6.0R, time 240h, squeeze 6 bars | +47 | +35 | +12 | 74 | 32% | -60 | 5/8 | 37% | -21 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +46 | +9 | +37 | 78 | 37% | -60 | 5/8 | 37% | -4 |

## bbsq_pro
4 of 144 distinct settings make money in both halves.
Current: P&L £+53 (train +57, test -4), 134 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +27 | +24 | +3 | 78 | 31% | -10 | 5/8 | 8% | +4 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +47 | +46 | +1 | 77 | 36% | -9 | 5/8 | 8% | +42 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 6 bars | +4 | +1 | +2 | 78 | 35% | -9 | 4/8 | 9% | -1 |
| stop 2.0ATR, target 4.0R, time 240h, squeeze 6 bars | +1 | +1 | +0 | 83 | 31% | -10 | 4/8 | 9% | -14 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+31 (train +137, test -107), 355 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+25 (train +44, test -19), 354 trades, worst month £-20

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
