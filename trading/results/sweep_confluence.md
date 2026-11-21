# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-21 07:34 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-22, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
0 of 1728 settings make money in both halves; 0 of 0 stress-tested top ones survive 2x fees.
Current setting: P&L £-104 (train -104, test +0), 23 trades, worst month £-62

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | | |

## pionex_majors (£200 start)
289 of 1728 settings make money in both halves; 9 of 9 stress-tested top ones survive 2x fees.
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
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +831 | +523 | +308 | 104 | 36% | +35 | -136 | 15/24 | 51% | - |

## funded ($10000 start)
568 of 1728 settings make money in both halves; 12 of 12 stress-tested top ones survive 2x fees.
Current setting: P&L $+2658 (train +751, test +1907), 109 trades, worst month $-579, 2 passes / 0 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +11269 | +6362 | +4907 | 338 | 26% | +470 | -1403 | 12/24 | 37% | +9542 | 13/7 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +9321 | +5463 | +3858 | 272 | 36% | +388 | -1322 | 14/24 | 25% | +7730 | 10/4 |
| stop 3.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +7599 | +4551 | +3049 | 260 | 42% | +317 | -1303 | 16/24 | 17% | +6427 | 8/2 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +7759 | +4207 | +3552 | 176 | 32% | +323 | -823 | 13/24 | 24% | +6469 | 8/3 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 20/80 | +6256 | +4187 | +2069 | 236 | 35% | +261 | -1132 | 15/24 | 19% | +4973 | 7/4 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +7315 | +3950 | +3365 | 350 | 27% | +305 | -1403 | 14/24 | 23% | - | 10/5 |
| stop 2.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +6357 | +3945 | +2412 | 308 | 32% | +265 | -1150 | 11/24 | 21% | - | 11/7 |
| stop 4.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +6952 | +3701 | +3251 | 231 | 44% | +290 | -1032 | 16/24 | 16% | - | 7/2 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.