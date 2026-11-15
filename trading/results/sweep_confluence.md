# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-15 11:38 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-17, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
3 of 1728 settings make money in both halves; 0 of 3 stress-tested top ones survive 2x fees.
Current setting: P&L £-119 (train -119, test +0), 50 trades, worst month £-195

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 2.0R, time 120h, window 8, trend off, zone 30/70 | +1017 | +686 | +331 | 942 | 38% | +41 | -336 | 15/25 | 73% | -130 |
| stop 2.5ATR, target 2.0R, time 120h, window 8, trend off, zone 20/80 | +792 | +604 | +188 | 885 | 38% | +32 | -310 | 17/25 | 85% | -112 |
| stop 2.0ATR, target 1.5R, time 120h, window 2, trend off, zone 20/80 | +275 | +208 | +67 | 327 | 44% | +11 | -173 | 13/24 | 70% | -103 |

## pionex_majors (£200 start)
306 of 1728 settings make money in both halves; 6 of 8 stress-tested top ones survive 2x fees.
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
736 of 1728 settings make money in both halves; 13 of 13 stress-tested top ones survive 2x fees.
Current setting: P&L $+2808 (train +1867, test +941), 117 trades, worst month $-750, 3 passes / 1 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +11811 | +6787 | +5024 | 338 | 27% | +472 | -1400 | 12/25 | 31% | +7158 | 12/5 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +11109 | +5784 | +5325 | 294 | 32% | +463 | -1320 | 14/24 | 20% | +6648 | 9/2 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +8109 | +5200 | +2909 | 355 | 27% | +324 | -1400 | 14/25 | 22% | +3987 | 12/8 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +8191 | +5182 | +3009 | 183 | 32% | +328 | -957 | 13/25 | 26% | +5944 | 8/4 |
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +8564 | +6088 | +2477 | 268 | 35% | +357 | -1313 | 14/24 | 23% | +7081 | 10/5 |
| stop 1.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +9539 | +4912 | +4628 | 393 | 18% | +382 | -1800 | 14/25 | 26% | - | 10/7 |
| stop 3.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +7155 | +4656 | +2499 | 248 | 38% | +298 | -1311 | 15/24 | 22% | - | 8/4 |
| stop 2.0ATR, target 4.0R, time 120h, window 2, trend on, zone 30/70 | +6118 | +3760 | +2359 | 61 | 44% | +266 | -450 | 13/23 | 7% | - | 4/0 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.