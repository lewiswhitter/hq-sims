# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-27 08:56 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-29, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
2 of 1728 settings make money in both halves; 0 of 2 stress-tested top ones survive 2x fees.
Current setting: P&L £-104 (train -104, test +0), 23 trades, worst month £-62

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 8.0R, time 48h, window 3, trend off, zone 20/80 | +324 | +253 | +71 | 573 | 25% | +13 | -390 | 14/24 | 90% | -116 |
| stop 2.0ATR, target 1.5R, time 120h, window 2, trend off, zone 20/80 | +237 | +222 | +15 | 336 | 44% | +10 | -173 | 13/24 | 70% | -103 |

## pionex_majors (£200 start)
319 of 1728 settings make money in both halves; 9 of 10 stress-tested top ones survive 2x fees.
Current setting: P&L £+609 (train +287, test +321), 120 trades, worst month £-134

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +1106 | +729 | +377 | 115 | 31% | +46 | -156 | 15/24 | 42% | +795 |
| stop 1.5ATR, target 5.0R, time 48h, window 3, trend on, zone 30/70 | +941 | +621 | +320 | 116 | 33% | +39 | -136 | 14/24 | 43% | +639 |
| stop 1.5ATR, target 5.0R, time 120h, window 3, trend on, zone 30/70 | +922 | +586 | +336 | 110 | 32% | +38 | -140 | 13/24 | 40% | +634 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend on, zone 30/70 | +1006 | +584 | +422 | 103 | 38% | +42 | -140 | 16/24 | 40% | +787 |
| stop 2.0ATR, target 4.0R, time 120h, window 2, trend on, zone 30/70 | +888 | +547 | +340 | 62 | 45% | +39 | -77 | 13/23 | 42% | +743 |
| stop 1.0ATR, target 8.0R, time 120h, window 3, trend on, zone 30/70 | +932 | +536 | +395 | 114 | 22% | +39 | -156 | 11/24 | 40% | - |
| stop 1.5ATR, target 8.0R, time 120h, window 3, trend on, zone 30/70 | +1082 | +531 | +550 | 108 | 28% | +45 | -160 | 12/24 | 50% | - |
| stop 3.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +1016 | +530 | +486 | 243 | 36% | +42 | -245 | 15/24 | 73% | - |

## funded ($10000 start)
596 of 1728 settings make money in both halves; 12 of 12 stress-tested top ones survive 2x fees.
Current setting: P&L $+2658 (train +751, test +1907), 109 trades, worst month $-579, 2 passes / 0 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +13203 | +7462 | +5741 | 337 | 27% | +550 | -911 | 12/24 | 32% | +10672 | 14/6 |
| stop 1.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +14609 | +5306 | +9303 | 391 | 18% | +609 | -1741 | 13/24 | 27% | +8201 | 14/8 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +9519 | +5089 | +4431 | 276 | 36% | +397 | -1037 | 13/24 | 29% | +8015 | 10/4 |
| stop 3.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +8302 | +4870 | +3432 | 260 | 43% | +346 | -982 | 16/24 | 13% | +6975 | 8/2 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +8635 | +4623 | +4011 | 349 | 27% | +360 | -960 | 14/24 | 19% | +6694 | 8/2 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 20/80 | +7088 | +4545 | +2543 | 236 | 36% | +295 | -992 | 15/24 | 18% | - | 7/3 |
| stop 2.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +7226 | +4346 | +2880 | 309 | 32% | +301 | -738 | 12/24 | 19% | - | 10/5 |
| stop 3.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +8214 | +4335 | +3879 | 247 | 38% | +342 | -1004 | 14/24 | 19% | - | 9/4 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.