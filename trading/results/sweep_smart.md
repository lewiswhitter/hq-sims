# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-11 19:50 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-06, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-27 (train +41, test -68), 127 trades, worst month £-59

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-9 (train +4, test -13), 118 trades, worst month £-12

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
3 of 144 distinct settings make money in both halves.
Current: P&L £+204 (train +227, test -23), 135 trades, worst month £-65

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +100 | +69 | +31 | 79 | 30% | -65 | 6/8 | 40% | +91 |
| stop 2.5ATR, target 6.0R, time 240h, squeeze 6 bars | +47 | +35 | +12 | 74 | 32% | -60 | 5/8 | 37% | -21 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +46 | +9 | +37 | 78 | 37% | -60 | 5/8 | 37% | -4 |

## bbsq_pro
3 of 144 distinct settings make money in both halves.
Current: P&L £+52 (train +57, test -5), 135 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +26 | +24 | +2 | 79 | 30% | -10 | 5/8 | 8% | +3 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +47 | +46 | +1 | 77 | 36% | -9 | 5/8 | 8% | +42 |
| stop 2.5ATR, target 3.0R, time 240h, squeeze 6 bars | +4 | +1 | +2 | 78 | 35% | -9 | 4/8 | 9% | -1 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+38 (train +133, test -95), 356 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+26 (train +44, test -17), 355 trades, worst month £-20

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
