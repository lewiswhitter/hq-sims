# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-11 19:50 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-13, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
2 of 1728 settings make money in both halves; 1 of 2 stress-tested top ones survive 2x fees.
Current setting: P&L £-115 (train -115, test +0), 50 trades, worst month £-194

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 2.0R, time 120h, window 8, trend off, zone 30/70 | +826 | +725 | +101 | 943 | 38% | +33 | -336 | 15/25 | 71% | -153 |
| stop 2.5ATR, target 8.0R, time 120h, window 8, trend on, zone 30/70 | +746 | +697 | +49 | 624 | 26% | +30 | -508 | 11/25 | 61% | +201 |

## pionex_majors (£200 start)
318 of 1728 settings make money in both halves; 5 of 7 stress-tested top ones survive 2x fees.
Current setting: P&L £+581 (train +419, test +162), 116 trades, worst month £-140

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +885 | +592 | +293 | 104 | 37% | +37 | -140 | 15/24 | 45% | +655 |
| stop 2.0ATR, target 5.0R, time 48h, window 3, trend on, zone 30/70 | +743 | +483 | +260 | 105 | 36% | +31 | -135 | 15/24 | 52% | +518 |
| stop 2.0ATR, target 8.0R, time 24h, window 3, trend on, zone 30/70 | +776 | +442 | +335 | 112 | 43% | +31 | -140 | 13/25 | 42% | +549 |
| stop 2.0ATR, target 4.0R, time 48h, window 2, trend on, zone 30/70 | +739 | +434 | +304 | 65 | 43% | +32 | -66 | 13/23 | 52% | -114 |
| stop 1.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +751 | +431 | +320 | 120 | 24% | +30 | -124 | 12/25 | 54% | -104 |
| stop 2.0ATR, target 4.0R, time 48h, window 3, trend on, zone 30/70 | +740 | +530 | +211 | 105 | 37% | +31 | -136 | 15/24 | 50% | - |
| stop 2.5ATR, target 8.0R, time 24h, window 3, trend on, zone 30/70 | +702 | +406 | +295 | 111 | 45% | +28 | -113 | 14/25 | 40% | - |
| stop 2.5ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +642 | +450 | +192 | 103 | 38% | +27 | -106 | 14/24 | 48% | - |

## funded ($10000 start)
658 of 1728 settings make money in both halves; 9 of 10 stress-tested top ones survive 2x fees.
Current setting: P&L $+2907 (train +2097, test +810), 116 trades, worst month $-700, 3 passes / 1 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +7731 | +4133 | +3597 | 343 | 27% | +309 | -1400 | 14/25 | 35% | +3401 | 11/6 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +5650 | +3544 | +2106 | 300 | 30% | +226 | -1400 | 16/25 | 23% | +3088 | 9/6 |
| stop 1.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +7445 | +3307 | +4138 | 400 | 18% | +298 | -1720 | 14/25 | 30% | -476 | 13/9 |
| stop 1.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +4929 | +3320 | +1609 | 120 | 24% | +197 | -800 | 12/25 | 12% | +2762 | 4/1 |
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +4437 | +2974 | +1464 | 104 | 37% | +185 | -700 | 15/24 | 11% | +3326 | 4/1 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +4364 | +2910 | +1454 | 360 | 27% | +175 | -1400 | 15/25 | 25% | - | 9/6 |
| stop 1.5ATR, target 8.0R, time 48h, window 5, trend on, zone 30/70 | +4588 | +2679 | +1908 | 229 | 28% | +184 | -1018 | 14/25 | 15% | - | 5/3 |
| stop 2.0ATR, target 4.0R, time 120h, window 2, trend on, zone 30/70 | +4096 | +2767 | +1328 | 61 | 44% | +178 | -400 | 13/23 | 7% | - | 3/0 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.