# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-14 06:52 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-15, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
2 of 1728 settings make money in both halves; 0 of 2 stress-tested top ones survive 2x fees.
Current setting: P&L £-115 (train -115, test +0), 50 trades, worst month £-194

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 1.5R, time 120h, window 2, trend off, zone 20/80 | +272 | +234 | +39 | 327 | 44% | +11 | -173 | 14/25 | 65% | -102 |
| stop 2.5ATR, target 2.0R, time 120h, window 8, trend off, zone 20/80 | +683 | +669 | +14 | 885 | 37% | +27 | -310 | 17/25 | 87% | -116 |

## pionex_majors (£200 start)
328 of 1728 settings make money in both halves; 8 of 9 stress-tested top ones survive 2x fees.
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
734 of 1728 settings make money in both halves; 14 of 14 stress-tested top ones survive 2x fees.
Current setting: P&L $+2808 (train +1867, test +941), 117 trades, worst month $-750, 3 passes / 1 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +11447 | +6034 | +5413 | 342 | 27% | +458 | -1400 | 12/25 | 33% | +6887 | 12/6 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +8341 | +5332 | +3009 | 182 | 33% | +334 | -800 | 13/25 | 24% | +5872 | 8/4 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +9259 | +6623 | +2636 | 269 | 36% | +370 | -1373 | 15/25 | 21% | +7279 | 11/5 |
| stop 3.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +7972 | +5339 | +2632 | 247 | 39% | +319 | -1103 | 17/25 | 15% | +5852 | 8/3 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +10724 | +5202 | +5522 | 297 | 31% | +429 | -1400 | 14/25 | 23% | +6374 | 10/4 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +7887 | +4589 | +3297 | 357 | 27% | +315 | -1400 | 14/25 | 24% | - | 12/8 |
| stop 2.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +7319 | +5161 | +2159 | 308 | 33% | +293 | -1025 | 13/25 | 21% | - | 10/5 |
| stop 1.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +8723 | +4093 | +4630 | 398 | 17% | +349 | -1800 | 14/25 | 28% | - | 13/11 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.