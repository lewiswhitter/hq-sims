# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-12 22:39 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-14, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
0 of 1728 settings make money in both halves; 0 of 0 stress-tested top ones survive 2x fees.
Current setting: P&L £-115 (train -115, test +0), 50 trades, worst month £-194

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| none pass | | | | | | | | | | |

## pionex_majors (£200 start)
324 of 1728 settings make money in both halves; 8 of 10 stress-tested top ones survive 2x fees.
Current setting: P&L £+598 (train +419, test +179), 117 trades, worst month £-140

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +885 | +592 | +293 | 104 | 37% | +37 | -140 | 15/24 | 45% | +655 |
| stop 2.0ATR, target 5.0R, time 48h, window 3, trend on, zone 30/70 | +756 | +483 | +273 | 106 | 37% | +32 | -135 | 15/24 | 52% | +528 |
| stop 2.0ATR, target 4.0R, time 48h, window 3, trend on, zone 30/70 | +753 | +530 | +224 | 106 | 38% | +31 | -136 | 15/24 | 50% | +531 |
| stop 2.0ATR, target 8.0R, time 24h, window 3, trend on, zone 30/70 | +776 | +442 | +335 | 112 | 43% | +31 | -140 | 13/25 | 42% | +549 |
| stop 2.0ATR, target 4.0R, time 48h, window 2, trend on, zone 30/70 | +739 | +434 | +304 | 65 | 43% | +32 | -66 | 13/23 | 52% | -114 |
| stop 1.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +776 | +431 | +344 | 121 | 25% | +31 | -124 | 12/25 | 54% | - |
| stop 2.5ATR, target 8.0R, time 24h, window 3, trend on, zone 30/70 | +702 | +406 | +295 | 111 | 45% | +28 | -113 | 14/25 | 40% | - |
| stop 2.5ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +642 | +450 | +192 | 103 | 38% | +27 | -106 | 14/24 | 48% | - |

## funded ($10000 start)
717 of 1728 settings make money in both halves; 15 of 15 stress-tested top ones survive 2x fees.
Current setting: P&L $+2808 (train +1867, test +941), 117 trades, worst month $-750, 3 passes / 1 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +9541 | +5934 | +3607 | 341 | 26% | +382 | -1400 | 12/25 | 34% | +5014 | 11/6 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +9213 | +5167 | +4046 | 296 | 31% | +369 | -1400 | 14/25 | 24% | +4998 | 10/4 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +7612 | +5332 | +2280 | 181 | 33% | +304 | -800 | 13/25 | 24% | +5204 | 8/4 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +7056 | +4489 | +2567 | 357 | 27% | +282 | -1400 | 14/25 | 26% | +3083 | 11/8 |
| stop 2.0ATR, target 4.0R, time 120h, window 2, trend on, zone 30/70 | +6118 | +3760 | +2359 | 61 | 44% | +266 | -450 | 13/23 | 7% | +4860 | 4/0 |
| stop 1.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +5843 | +3993 | +1850 | 397 | 17% | +234 | -1800 | 14/25 | 28% | - | 12/11 |
| stop 1.5ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +5742 | +3917 | +1825 | 113 | 32% | +239 | -750 | 14/24 | 12% | - | 4/1 |
| stop 2.5ATR, target 8.0R, time 48h, window 2, trend off, zone 20/80 | +5908 | +3553 | +2355 | 92 | 35% | +236 | -442 | 13/25 | 14% | - | 4/1 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.