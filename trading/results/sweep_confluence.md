# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-24 00:12 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-25, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
2 of 1728 settings make money in both halves; 1 of 2 stress-tested top ones survive 2x fees.
Current setting: P&L £-104 (train -104, test +0), 23 trades, worst month £-62

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 8.0R, time 120h, window 8, trend off, zone 30/70 | +3019 | +2397 | +622 | 1055 | 20% | +126 | -364 | 13/24 | 51% | +1395 |
| stop 2.0ATR, target 1.5R, time 120h, window 2, trend off, zone 20/80 | +237 | +222 | +15 | 336 | 44% | +10 | -173 | 13/24 | 70% | -103 |

## pionex_majors (£200 start)
302 of 1728 settings make money in both halves; 7 of 7 stress-tested top ones survive 2x fees.
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
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +920 | +523 | +397 | 106 | 37% | +38 | -136 | 15/24 | 51% | - |

## funded ($10000 start)
591 of 1728 settings make money in both halves; 11 of 12 stress-tested top ones survive 2x fees.
Current setting: P&L $+2658 (train +751, test +1907), 109 trades, worst month $-579, 2 passes / 0 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +12416 | +6478 | +5938 | 336 | 27% | +517 | -1315 | 12/24 | 35% | +10555 | 13/7 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +9920 | +5291 | +4628 | 272 | 36% | +413 | -1297 | 14/24 | 25% | +8439 | 10/4 |
| stop 3.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +8179 | +4549 | +3630 | 260 | 43% | +341 | -1105 | 16/24 | 15% | +6914 | 8/2 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 20/80 | +7287 | +4546 | +2741 | 236 | 36% | +304 | -1002 | 15/24 | 20% | +5567 | 7/3 |
| stop 2.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +7208 | +4130 | +3077 | 307 | 32% | +300 | -1053 | 11/24 | 20% | +6183 | 9/4 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +8317 | +4007 | +4310 | 175 | 32% | +347 | -780 | 13/24 | 27% | - | 9/3 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +8145 | +3937 | +4208 | 350 | 27% | +339 | -1315 | 14/24 | 22% | - | 10/5 |
| stop 3.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +8016 | +3741 | +4275 | 246 | 38% | +334 | -1105 | 14/24 | 23% | - | 9/5 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.