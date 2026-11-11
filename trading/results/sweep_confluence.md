# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-11 06:52 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-12, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
1 of 1728 settings make money in both halves; 0 of 1 stress-tested top ones survive 2x fees.
Current setting: P&L £-112 (train -112, test +0), 41 trades, worst month £-192

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 8.0R, time 120h, window 8, trend on, zone 30/70 | +605 | +555 | +49 | 627 | 26% | +24 | -508 | 11/25 | 69% | -127 |

## pionex_majors (£200 start)
230 of 1728 settings make money in both halves; 3 of 5 stress-tested top ones survive 2x fees.
Current setting: P&L £+562 (train +400, test +162), 117 trades, worst month £-139

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +866 | +574 | +293 | 105 | 36% | +35 | -138 | 15/25 | 47% | +632 |
| stop 2.0ATR, target 5.0R, time 48h, window 3, trend on, zone 30/70 | +711 | +451 | +260 | 106 | 36% | +28 | -134 | 15/25 | 55% | -106 |
| stop 2.0ATR, target 4.0R, time 48h, window 3, trend on, zone 30/70 | +710 | +499 | +211 | 106 | 37% | +28 | -134 | 15/25 | 53% | -102 |
| stop 2.0ATR, target 8.0R, time 24h, window 3, trend on, zone 30/70 | +756 | +422 | +335 | 113 | 42% | +30 | -140 | 13/25 | 44% | +529 |
| stop 2.5ATR, target 8.0R, time 24h, window 3, trend on, zone 30/70 | +682 | +386 | +295 | 112 | 45% | +27 | -113 | 14/25 | 42% | +500 |
| stop 2.5ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +623 | +431 | +192 | 104 | 38% | +25 | -105 | 14/25 | 51% | - |
| stop 2.5ATR, target 8.0R, time 48h, window 2, trend off, zone 20/80 | +675 | +369 | +306 | 93 | 34% | +27 | -88 | 13/25 | 66% | - |
| stop 4.0ATR, target 5.0R, time 48h, window 2, trend off, zone 20/80 | +555 | +357 | +198 | 92 | 42% | +22 | -58 | 14/25 | 42% | - |

## funded ($10000 start)
607 of 1728 settings make money in both halves; 11 of 12 stress-tested top ones survive 2x fees.
Current setting: P&L $+2807 (train +1997, test +810), 117 trades, worst month $-700, 3 passes / 1 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +7795 | +4197 | +3597 | 344 | 27% | +312 | -1236 | 14/25 | 34% | +3455 | 11/6 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +5505 | +3398 | +2106 | 301 | 30% | +220 | -1400 | 15/25 | 25% | +3038 | 8/5 |
| stop 1.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +4829 | +3220 | +1609 | 121 | 24% | +193 | -800 | 12/25 | 12% | +2662 | 4/1 |
| stop 1.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +7345 | +3207 | +4138 | 401 | 18% | +294 | -1720 | 14/25 | 30% | -233 | 13/9 |
| stop 1.5ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +4427 | +2974 | +1454 | 361 | 27% | +177 | -1236 | 15/25 | 24% | +842 | 9/6 |
| stop 2.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +4334 | +2871 | +1464 | 105 | 36% | +173 | -700 | 15/25 | 11% | +3223 | 4/1 |
| stop 2.0ATR, target 4.0R, time 120h, window 2, trend on, zone 30/70 | +3994 | +2666 | +1328 | 62 | 44% | +166 | -400 | 13/24 | 7% | - | 3/0 |
| stop 2.0ATR, target 4.0R, time 120h, window 3, trend off, zone 30/70 | +4458 | +3160 | +1298 | 180 | 32% | +178 | -800 | 13/25 | 17% | - | 6/3 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.