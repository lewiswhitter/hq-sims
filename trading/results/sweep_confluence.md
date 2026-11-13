# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-13 20:00 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-15, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
1 of 1728 settings make money in both halves; 0 of 1 stress-tested top ones survive 2x fees.
Current setting: P&L £-115 (train -115, test +0), 50 trades, worst month £-194

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 1.5R, time 120h, window 2, trend off, zone 20/80 | +244 | +234 | +11 | 326 | 44% | +10 | -173 | 14/25 | 65% | -102 |

## pionex_majors (£200 start)
334 of 1728 settings make money in both halves; 8 of 10 stress-tested top ones survive 2x fees.
Current setting: P&L £+598 (train +419, test +179), 117 trades, worst month £-140

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +885 | +592 | +293 | 104 | 37% | +37 | -140 | 15/24 | 45% | +655 |
| stop 2.0ATR, target 5.0R, time 48h, window 3, trend on, zone 30/70 | +756 | +483 | +273 | 106 | 37% | +32 | -135 | 15/24 | 52% | +528 |
| stop 2.0ATR, target 4.0R, time 48h, window 3, trend on, zone 30/70 | +753 | +530 | +224 | 106 | 38% | +31 | -136 | 15/24 | 50% | +531 |
| stop 2.0ATR, target 8.0R, time 24h, window 3, trend on, zone 30/70 | +776 | +442 | +335 | 112 | 43% | +31 | -140 | 13/25 | 42% | +549 |
| stop 2.0ATR, target 4.0R, time 48h, window 2, trend on, zone 30/70 | +739 | +434 | +304 | 65 | 43% | +32 | -66 | 13/23 | 52% | -114 |
| stop 1.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +776 | +431 | +344 | 121 | 25% | +31 | -124 | 12/25 | 54% | - |
| stop 1.0ATR, target 8.0R, time 120h, window 3, trend on, zone 30/70 | +712 | +414 | +298 | 112 | 21% | +28 | -147 | 11/25 | 55% | - |
| stop 2.5ATR, target 8.0R, time 24h, window 3, trend on, zone 30/70 | +702 | +406 | +295 | 111 | 45% | +28 | -113 | 14/25 | 40% | - |

## funded ($10000 start)
740 of 1728 settings make money in both halves; 15 of 15 stress-tested top ones survive 2x fees.
Current setting: P&L $+2808 (train +1867, test +941), 117 trades, worst month $-750, 3 passes / 1 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +11347 | +5934 | +5413 | 343 | 27% | +454 | -1400 | 12/25 | 34% | +6655 | 12/6 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +8341 | +5332 | +3009 | 182 | 33% | +334 | -800 | 13/25 | 24% | +5872 | 8/4 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +10689 | +5167 | +5522 | 298 | 31% | +428 | -1400 | 14/25 | 24% | +6365 | 10/4 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +8658 | +6110 | +2549 | 273 | 36% | +346 | -1717 | 15/25 | 27% | +6761 | 10/5 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +7787 | +4489 | +3297 | 358 | 27% | +311 | -1400 | 14/25 | 26% | +3752 | 12/8 |
| stop 2.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +7183 | +5024 | +2159 | 309 | 33% | +287 | -1048 | 13/25 | 21% | - | 10/5 |
| stop 3.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +7459 | +5397 | +2061 | 247 | 38% | +298 | -1134 | 17/25 | 17% | - | 7/3 |
| stop 1.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +8623 | +3993 | +4630 | 399 | 17% | +345 | -1800 | 14/25 | 28% | - | 13/11 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.