# CONFLUENCE sweep: 1728 settings x 3 books, last 730 days of 1h bars
Updated 2026-11-08 07:38 UTC on 16 free GitHub machines (public hq-sims repo) in 0 min. Paper maths only. Train = before 2026-03-09, test = after. 'Passes' = both halves make money; '2x fees' column = same setting with double fees (the top ones only).

## pionex (£200 start)
1 of 1728 settings make money in both halves; 0 of 1 stress-tested top ones survive 2x fees.
Current setting: P&L £-115 (train -115, test +0), 45 trades, worst month £-192

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 2.5ATR, target 8.0R, time 120h, window 8, trend on, zone 30/70 | +402 | +393 | +9 | 630 | 25% | +16 | -508 | 10/25 | 81% | -135 |

## pionex_majors (£200 start)
201 of 1728 settings make money in both halves; 5 of 6 stress-tested top ones survive 2x fees.
Current setting: P&L £+428 (train +354, test +74), 117 trades, worst month £-136

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees |
|---|---|---|---|---|---|---|---|---|---|---|
| stop 3.0ATR, target 3.0R, time 120h, window 2, trend off, zone 20/80 | +521 | +334 | +187 | 87 | 44% | +22 | -68 | 14/24 | 42% | +396 |
| stop 2.5ATR, target 8.0R, time 48h, window 2, trend off, zone 20/80 | +526 | +316 | +210 | 94 | 33% | +22 | -88 | 12/24 | 71% | -106 |
| stop 2.0ATR, target 8.0R, time 24h, window 3, trend on, zone 30/70 | +572 | +430 | +142 | 111 | 41% | +24 | -140 | 12/24 | 43% | +374 |
| stop 2.0ATR, target 4.0R, time 24h, window 3, trend on, zone 30/70 | +421 | +271 | +150 | 111 | 41% | +18 | -136 | 12/24 | 59% | +234 |
| stop 4.0ATR, target 5.0R, time 48h, window 2, trend off, zone 20/80 | +504 | +370 | +134 | 93 | 42% | +21 | -58 | 13/24 | 40% | +398 |
| stop 2.0ATR, target 5.0R, time 24h, window 3, trend on, zone 30/70 | +491 | +268 | +223 | 111 | 41% | +20 | -139 | 12/24 | 54% | - |
| stop 3.0ATR, target 5.0R, time 120h, window 2, trend off, zone 20/80 | +425 | +296 | +129 | 85 | 36% | +18 | -80 | 12/24 | 56% | - |
| stop 4.0ATR, target 8.0R, time 48h, window 2, trend off, zone 20/80 | +391 | +248 | +142 | 93 | 42% | +16 | -58 | 13/24 | 52% | - |

## funded ($10000 start)
396 of 1728 settings make money in both halves; 9 of 10 stress-tested top ones survive 2x fees.
Current setting: P&L $+2165 (train +1795, test +370), 117 trades, worst month $-700, 2 passes / 0 fails

| setting | P&L | train | test | trades | win% | per month | worst month | months up | max DD | 2x fees | pass/fail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| stop 1.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +6944 | +4010 | +2934 | 401 | 18% | +278 | -1720 | 14/25 | 28% | -1510 | 12/9 |
| stop 1.5ATR, target 5.0R, time 120h, window 5, trend off, zone 30/70 | +5692 | +2855 | +2837 | 349 | 25% | +228 | -1441 | 14/25 | 43% | +2642 | 11/7 |
| stop 2.0ATR, target 4.0R, time 120h, window 5, trend off, zone 30/70 | +4226 | +2762 | +1464 | 305 | 29% | +169 | -1540 | 16/25 | 31% | +2359 | 8/6 |
| stop 2.0ATR, target 8.0R, time 120h, window 2, trend on, zone 30/70 | +3493 | +2294 | +1199 | 60 | 35% | +152 | -500 | 10/23 | 9% | +2836 | 3/0 |
| stop 1.0ATR, target 8.0R, time 48h, window 3, trend on, zone 30/70 | +4133 | +3020 | +1113 | 121 | 23% | +172 | -800 | 11/24 | 12% | +2104 | 4/1 |
| stop 3.0ATR, target 8.0R, time 120h, window 5, trend off, zone 30/70 | +3333 | +2077 | +1256 | 236 | 33% | +133 | -1231 | 15/25 | 23% | - | 6/4 |
| stop 2.0ATR, target 8.0R, time 120h, window 2, trend off, zone 30/70 | +3153 | +2027 | +1126 | 116 | 28% | +131 | -800 | 13/24 | 20% | - | 4/2 |
| stop 2.0ATR, target 5.0R, time 120h, window 2, trend on, zone 30/70 | +2896 | +1925 | +971 | 61 | 36% | +126 | -500 | 12/23 | 10% | - | 2/0 |

Next: Claude picks the best robust setting per book for the 16 Nov review (research/ftmo-pionex-frameworks.md). Nothing changes in the live paper bots until Lewis says yes.