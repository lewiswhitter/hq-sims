# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-19 20:56 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-21, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
2 of 1728 settings make money in both halves; 1 of 2 stress-tested top ones survive 2x fees.
Current setting: P&L £-103 (train -103, test +0), 37 trades, worst month £-172

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 8.0R, time 120h, window 8, trend off, zone 30/70 | +2593 | +2294 | +299 | 1060 | 20% | +104 | -364 | 13/25 | 69% | +984 |
| stop 4.0ATR, target 4.0R, time 120h, window 8, trend off, zone 30/70 | +311 | +125 | +186 | 534 | 39% | +13 | -256 | 15/24 | 84% | -114 |

## pionex_majors (£200 start)
302 of 1728 settings make money in both halves; 8 of 8 stress-tested top ones survive 2x fees.
Current setting: P&L £+562 (train +350, test +212), 119 trades, worst month £-137

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +871 | +562 | +308 | 105 | 36% | +36 | -139 | 15/24 | 46% | +640 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend on, zone 30/70 | +832 | +560 | +272 | 102 | 36% | +35 | -140 | 16/24 | 50% | +625 |
| stop 2.0ATR, target 4.0R, time 120h, window 2, trend on, zone 30/70 | +813 | +547 | +266 | 61 | 44% | +35 | -77 | 13/23 | 42% | +672 |
| stop 1.5ATR, target 8.0R, time 120h, window 3, trend on, zone 30/70 | +750 | +493 | +256 | 107 | 26% | +31 | -160 | 12/24 | 54% | +463 |
| stop 2.0ATR, target 8.0R, time 120h, window 2, trend on, zone 30/70 | +986 | +483 | +503 | 60 | 38% | +43 | -100 | 11/23 | 46% | +823 |
| stop 2.0ATR, target 4.0R, time 48h, window 3, trend on, zone 30/70 | +733 | +494 | +239 | 107 | 37% | +31 | -135 | 15/24 | 52% | - |
| stop 1.0ATR, target 8.0R, time 120h, window 3, trend on, zone 30/70 | +721 | +463 | +258 | 114 | 21% | +29 | -154 | 11/25 | 49% | - |
| stop 2.0ATR, target 5.0R, time 48h, window 3, trend on, zone 30/70 | +735 | +446 | +289 | 107 | 36% | +31 | -134 | 15/24 | 53% | - |

## funded ($10000 start)
511 of 1728 settings make money in both halves; 10 of 11 stress-tested top ones survive 2x fees.
Current setting: P&L $+2049 (train +974, test +1075), 108 trades, worst month $-579, 2 passes / 1 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +8652 | +5463 | +3190 | 271 | 35% | +361 | -1415 | 14/24 | 26% | +7084 | 10/4 |
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +9078 | +5186 | +3892 | 341 | 25% | +363 | -1509 | 12/25 | 44% | +8933 | 13/8 |
| stop 3.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +6827 | +4642 | +2185 | 259 | 42% | +284 | -1310 | 16/24 | 17% | +5696 | 7/2 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +6983 | +4185 | +2798 | 175 | 31% | +279 | -780 | 13/25 | 24% | +5687 | 8/3 |
| stop 4.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +6202 | +3833 | +2369 | 230 | 44% | +258 | -1009 | 16/24 | 16% | +5276 | 6/2 |
| stop 3.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +6586 | +3760 | +2826 | 246 | 37% | +274 | -1310 | 14/24 | 26% | - | 8/5 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +6288 | +3753 | +2536 | 351 | 26% | +252 | -1509 | 14/25 | 26% | - | 9/5 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +7743 | +3493 | +4250 | 296 | 29% | +323 | -1540 | 13/24 | 29% | - | 8/4 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.