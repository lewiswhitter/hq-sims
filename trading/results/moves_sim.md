# Big-move scenario farm (115,200 scenarios, 10 coins, 747 days of 1m data)

**Verdict:** NO RELIABLE EDGE: 157 scenarios passed the pick + confirm periods (~61 by luck; similar scenarios share trades so they pass in clusters), and 0 held up in the newest period.

- Scenarios tested: 115,200; with enough trades in every period: 115,200
- Up with t>=2 in A (oldest half, pick): 4,204
- ...and in B (next quarter, confirm): 157 (luck alone ~61, rough: scenarios share trades)
- ...and in C (newest quarter, final): 0
- Costs: taker 0.045% + 0.02% slippage per market fill, maker 0.015%. 'C 2x' = C with costs doubled.

Where the A+B survivors came from: bar: {1: 0, 15: 48, 3: 0, 30: 96, 5: 0, 60: 13}; mode: {'fade': 0, 'follow': 157}; entry: {'limit': 60, 'market': 97}; vol: {0: 0, 1.5: 0, 2: 3, 3: 2, 5: 152}

## Top 30 A+B survivors and their final (C) result
| scenario | A avg % (t) | B avg % (t) | **C avg %** (t) | C 2x costs | C trades/day | C shorts avg % | C longs avg % |
|---|---|---|---|---|---|---|---|
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.674 (3.7) | +0.205 (3.3) | **-0.122** (-3.4) | -0.252 | 3.6 | -0.172 | -0.043 |
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.663 (3.7) | +0.199 (3.2) | **-0.125** (-3.5) | -0.255 | 3.6 | -0.175 | -0.046 |
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.663 (3.7) | +0.199 (3.2) | **-0.125** (-3.5) | -0.255 | 3.6 | -0.175 | -0.046 |
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.663 (3.7) | +0.199 (3.2) | **-0.125** (-3.5) | -0.255 | 3.6 | -0.175 | -0.045 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.624 (3.7) | +0.181 (3.0) | **-0.118** (-3.4) | -0.248 | 3.7 | -0.166 | -0.041 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.703 (3.6) | +0.209 (3.0) | **-0.109** (-2.8) | -0.239 | 3.3 | -0.177 | +0.000 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.691 (3.6) | +0.203 (2.9) | **-0.112** (-2.8) | -0.242 | 3.3 | -0.180 | -0.003 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.691 (3.6) | +0.203 (2.9) | **-0.112** (-2.8) | -0.242 | 3.3 | -0.180 | -0.003 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.691 (3.6) | +0.203 (2.9) | **-0.112** (-2.8) | -0.242 | 3.3 | -0.180 | -0.002 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.613 (3.6) | +0.175 (2.9) | **-0.122** (-3.5) | -0.252 | 3.7 | -0.170 | -0.045 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.613 (3.6) | +0.175 (2.9) | **-0.122** (-3.5) | -0.252 | 3.7 | -0.170 | -0.045 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.614 (3.6) | +0.174 (2.9) | **-0.120** (-3.4) | -0.250 | 3.7 | -0.168 | -0.044 |
| 30m break 12 bars, vol 5x, follow, market, stop 1.5 ATR, TP none, trail on, hold 6 bars | +0.569 (3.4) | +0.188 (2.8) | **-0.182** (-4.5) | -0.312 | 3.7 | -0.239 | -0.091 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.807 (3.5) | +0.235 (2.8) | **-0.133** (-2.8) | -0.263 | 2.6 | -0.224 | +0.008 |
| 30m break 48 bars, vol 5x, follow, market, stop 1.5 ATR, TP none, trail on, hold 6 bars | +0.641 (3.4) | +0.213 (2.8) | **-0.184** (-4.2) | -0.314 | 3.3 | -0.267 | -0.052 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.396 (2.8) | +0.241 (2.8) | **-0.064** (-1.5) | -0.144 | 2.9 | -0.030 | -0.122 |
| 30m break 24 bars, vol 5x, follow, market, stop 1.5 ATR, TP none, trail on, hold 6 bars | +0.616 (3.4) | +0.194 (2.8) | **-0.195** (-4.8) | -0.325 | 3.6 | -0.259 | -0.093 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.793 (3.4) | +0.232 (2.8) | **-0.137** (-2.9) | -0.267 | 2.6 | -0.228 | +0.004 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.793 (3.4) | +0.232 (2.8) | **-0.137** (-2.9) | -0.267 | 2.6 | -0.228 | +0.004 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.793 (3.4) | +0.232 (2.8) | **-0.137** (-2.9) | -0.267 | 2.6 | -0.228 | +0.006 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 48 bars | +0.391 (2.8) | +0.238 (2.7) | **-0.072** (-1.7) | -0.152 | 2.9 | -0.037 | -0.133 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 144 bars | +0.391 (2.8) | +0.238 (2.7) | **-0.072** (-1.7) | -0.152 | 2.9 | -0.037 | -0.133 |
| 30m break 24 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 48 bars | +0.386 (2.9) | +0.214 (2.7) | **-0.082** (-2.1) | -0.162 | 3.1 | -0.040 | -0.156 |
| 30m break 24 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 144 bars | +0.386 (2.9) | +0.214 (2.7) | **-0.082** (-2.1) | -0.162 | 3.1 | -0.040 | -0.156 |
| 30m break 48 bars, vol 5x, follow, market, stop 2 ATR, TP none, trail on, hold 6 bars | +0.564 (3.0) | +0.222 (2.7) | **-0.267** (-5.5) | -0.397 | 3.3 | -0.361 | -0.117 |
| 30m break 12 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.359 (2.9) | +0.201 (2.7) | **-0.066** (-1.7) | -0.146 | 3.2 | -0.018 | -0.148 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 12 bars | +0.392 (2.8) | +0.235 (2.7) | **-0.072** (-1.7) | -0.152 | 2.9 | -0.037 | -0.131 |
| 30m break 24 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.390 (3.0) | +0.211 (2.7) | **-0.075** (-2.0) | -0.155 | 3.1 | -0.034 | -0.145 |
| 15m break 192 bars, vol 5x, follow, market, stop 3 ATR, TP 1R, trail off, hold 12 bars | +0.253 (4.0) | +0.154 (2.7) | **-0.210** (-4.2) | -0.326 | 4.2 | -0.232 | -0.176 |
| 30m break 12 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 48 bars | +0.360 (2.9) | +0.199 (2.7) | **-0.073** (-1.9) | -0.153 | 3.2 | -0.023 | -0.158 |

## What picking the best-looking (A only) would have done
| scenario | A avg % | C avg % |
|---|---|---|
| 60m break 96 bars, vol 5x, follow, limit, stop 3 ATR, TP 3R, trail off, hold 144 bars | +1.760 | +0.149 |
| 60m break 192 bars, vol 5x, follow, limit, stop 3 ATR, TP none, trail on, hold 144 bars | +1.709 | +0.129 |
| 60m break 96 bars, vol 5x, follow, limit, stop 3 ATR, TP none, trail on, hold 144 bars | +1.701 | +0.306 |
| 30m break 288 bars, vol 5x, follow, market, stop 3 ATR, TP none, trail on, hold 144 bars | +1.658 | -0.436 |
| 30m break 288 bars, vol 5x, follow, market, stop 3 ATR, TP none, trail on, hold 48 bars | +1.625 | -0.484 |

Per trade % is of the position. At 30% of the account x 10x, account % per trade = 3x that.
