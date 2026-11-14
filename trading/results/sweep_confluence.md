# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-14 18:25 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-16, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
3 of 1728 settings make money in both halves; 0 of 3 stress-tested top ones survive 2x fees.
Current setting: P&L £-115 (train -115, test +0), 50 trades, worst month £-194

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 2.0R, time 120h, window 8, trend off, zone 30/70 | +932 | +600 | +331 | 945 | 38% | +37 | -336 | 15/25 | 81% | -126 |
| stop 2.5ATR, target 2.0R, time 120h, window 8, trend off, zone 20/80 | +785 | +597 | +188 | 888 | 38% | +31 | -310 | 17/25 | 85% | -104 |
| stop 2.0ATR, target 1.5R, time 120h, window 2, trend off, zone 20/80 | +301 | +234 | +67 | 328 | 45% | +12 | -173 | 14/25 | 65% | -102 |

## pionex_majors (£200 start)
331 of 1728 settings make money in both halves; 7 of 8 stress-tested top ones survive 2x fees.
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
746 of 1728 settings make money in both halves; 13 of 13 stress-tested top ones survive 2x fees.
Current setting: P&L $+2808 (train +1867, test +941), 117 trades, worst month $-750, 3 passes / 1 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +11795 | +6383 | +5413 | 339 | 27% | +472 | -1316 | 12/25 | 31% | +6943 | 12/5 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +8341 | +5332 | +3009 | 182 | 33% | +334 | -800 | 13/25 | 24% | +5872 | 8/4 |
| stop 3.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +7932 | +5300 | +2632 | 246 | 39% | +317 | -1104 | 17/25 | 16% | +5958 | 9/4 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +8657 | +6108 | +2549 | 271 | 36% | +346 | -1577 | 15/25 | 26% | +6785 | 10/5 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +8093 | +4796 | +3297 | 356 | 27% | +324 | -1316 | 14/25 | 22% | +3946 | 12/8 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +10313 | +4791 | +5522 | 294 | 31% | +413 | -1400 | 14/25 | 21% | - | 10/4 |
| stop 2.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +6924 | +4765 | +2159 | 309 | 33% | +277 | -1218 | 12/25 | 22% | - | 10/6 |
| stop 1.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +8462 | +3834 | +4628 | 397 | 18% | +338 | -1800 | 14/25 | 29% | - | 10/8 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.