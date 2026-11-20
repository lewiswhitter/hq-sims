# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-20 07:38 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-21, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
0 of 1728 settings make money in both halves; 0 of 0 stress-tested top ones survive 2x fees.
Current setting: P&L £-104 (train -104, test +0), 23 trades, worst month £-62

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | | |

## pionex_majors (£200 start)
279 of 1728 settings make money in both halves; 9 of 9 stress-tested top ones survive 2x fees.
Current setting: P&L £+499 (train +287, test +212), 118 trades, worst month £-134

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend on, zone 30/70 | +856 | +584 | +272 | 101 | 37% | +36 | -140 | 16/24 | 40% | +646 |
| stop 2.0ATR, target 4.0R, time 120h, window 2, trend on, zone 30/70 | +813 | +547 | +266 | 61 | 44% | +35 | -77 | 13/23 | 42% | +672 |
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +831 | +523 | +308 | 104 | 36% | +35 | -136 | 15/24 | 51% | +595 |
| stop 1.0ATR, target 8.0R, time 120h, window 3, trend on, zone 30/70 | +794 | +536 | +258 | 113 | 21% | +33 | -156 | 11/24 | 40% | +405 |
| stop 1.5ATR, target 8.0R, time 120h, window 3, trend on, zone 30/70 | +788 | +531 | +256 | 106 | 26% | +33 | -160 | 12/24 | 50% | +499 |
| stop 2.0ATR, target 8.0R, time 120h, window 3, trend on, zone 30/70 | +745 | +497 | +248 | 95 | 31% | +31 | -133 | 12/24 | 71% | - |
| stop 2.0ATR, target 8.0R, time 120h, window 2, trend on, zone 30/70 | +986 | +483 | +503 | 60 | 38% | +43 | -100 | 11/23 | 46% | - |
| stop 2.0ATR, target 4.0R, time 48h, window 3, trend on, zone 30/70 | +678 | +439 | +239 | 106 | 37% | +28 | -131 | 15/24 | 57% | - |

## funded ($10000 start)
511 of 1728 settings make money in both halves; 10 of 10 stress-tested top ones survive 2x fees.
Current setting: P&L $+1831 (train +751, test +1080), 107 trades, worst month $-579, 1 passes / 0 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +10213 | +6321 | +3892 | 336 | 26% | +426 | -1553 | 13/24 | 38% | +8618 | 13/7 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +8653 | +5463 | +3190 | 271 | 35% | +361 | -1415 | 14/24 | 26% | +7084 | 10/4 |
| stop 3.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +7015 | +4831 | +2185 | 259 | 42% | +292 | -1119 | 16/24 | 16% | +5778 | 7/2 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +7005 | +4207 | +2798 | 174 | 31% | +292 | -823 | 13/24 | 24% | +5755 | 8/3 |
| stop 3.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +6849 | +4023 | +2826 | 246 | 37% | +285 | -1119 | 14/24 | 24% | +5648 | 8/5 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +6797 | +3901 | +2895 | 350 | 26% | +283 | -1553 | 14/24 | 25% | - | 9/5 |
| stop 4.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +6129 | +3761 | +2369 | 231 | 44% | +255 | -1108 | 16/24 | 17% | - | 6/2 |
| stop 2.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +5791 | +4040 | +1751 | 306 | 31% | +241 | -1248 | 12/24 | 21% | - | 11/7 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.