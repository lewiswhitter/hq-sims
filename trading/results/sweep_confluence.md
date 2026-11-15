# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-15 19:07 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-17, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

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
551 of 1728 settings make money in both halves; 11 of 11 stress-tested top ones survive 2x fees.
Current setting: P&L $+2291 (train +1287, test +1004), 106 trades, worst month $-589, 2 passes / 1 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +8949 | +5609 | +3339 | 269 | 36% | +373 | -1416 | 14/24 | 26% | +7375 | 10/4 |
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +9567 | +5477 | +4090 | 337 | 26% | +383 | -1511 | 12/25 | 44% | +9407 | 13/8 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +7277 | +4281 | +2996 | 173 | 31% | +291 | -780 | 13/25 | 24% | +5973 | 8/3 |
| stop 3.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +6839 | +4802 | +2037 | 259 | 42% | +285 | -1299 | 16/24 | 17% | +5694 | 7/2 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +6778 | +4044 | +2734 | 347 | 26% | +271 | -1511 | 14/25 | 26% | +5322 | 9/5 |
| stop 4.0ATR, target 2.0R, time 120h, window 5, trend off, zone 30/70 | +6202 | +3982 | +2220 | 230 | 44% | +258 | -1009 | 16/24 | 16% | - | 6/2 |
| stop 3.0ATR, target 3.0R, time 120h, window 5, trend off, zone 30/70 | +6598 | +3920 | +2678 | 246 | 37% | +275 | -1299 | 14/24 | 26% | - | 8/5 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +8038 | +3639 | +4399 | 294 | 29% | +335 | -1541 | 13/24 | 29% | - | 8/4 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.