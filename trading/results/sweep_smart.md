# SMART sweep: 1296 settings, last 200 days (Hyperliquid 1h/4h + real funding, £200 per book)
Updated 2026-11-09 22:37 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-09-04, test = after. '2x fees' = same setting with double fees.

## trend_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £-65 (train +13, test -78), 129 trades, worst month £-75

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## trend_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £-17 (train -3, test -14), 120 trades, worst month £-15

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## bbsq_lewis
3 of 144 distinct settings make money in both halves.
Current: P&L £+194 (train +232, test -38), 132 trades, worst month £-65

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +105 | +74 | +31 | 78 | 31% | -65 | 6/8 | 40% | +96 |
| stop 2.5ATR, target 6.0R, time 240h, squeeze 6 bars | +47 | +35 | +12 | 74 | 32% | -60 | 5/8 | 37% | -21 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +46 | +9 | +37 | 78 | 37% | -60 | 5/8 | 37% | -4 |

## bbsq_pro
2 of 144 distinct settings make money in both halves.
Current: P&L £+51 (train +58, test -8), 132 trades, worst month £-10

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 6.0R, time 240h, squeeze 6 bars | +27 | +24 | +2 | 78 | 31% | -10 | 5/8 | 8% | +4 |
| stop 2.5ATR, target 4.0R, time 240h, squeeze 6 bars | +47 | +46 | +1 | 77 | 36% | -9 | 5/8 | 8% | +42 |

## movers_lewis
0 of 3 distinct settings make money in both halves.
Current: P&L £+30 (train +148, test -119), 356 trades, worst month £-110

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |

## movers_pro
0 of 3 distinct settings make money in both halves.
Current: P&L £+22 (train +44, test -21), 355 trades, worst month £-19

| setting | P&L | train | test | trades | win% | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | |
