# Big-move scenario farm (115,200 scenarios, 10 coins, 746 days of 1m data)

**Verdict:** NO RELIABLE EDGE: 166 scenarios passed the pick + confirm periods (~61 by luck; similar scenarios share trades so they pass in clusters), and 0 held up in the newest period.

- Scenarios tested: 115,200; with enough trades in every period: 115,200
- Up with t>=2 in A (oldest half, pick): 4,205
- ...and in B (next quarter, confirm): 166 (luck alone ~61, rough: scenarios share trades)
- ...and in C (newest quarter, final): 0
- Costs: taker 0.045% + 0.02% slippage per market fill, maker 0.015%. 'C 2x' = C with costs doubled.

Where the A+B survivors came from: bar: {1: 0, 15: 50, 3: 0, 30: 101, 5: 0, 60: 15}; mode: {'fade': 0, 'follow': 166}; entry: {'limit': 64, 'market': 102}; vol: {0: 0, 1.5: 0, 2: 4, 3: 3, 5: 159}

## Top 30 A+B survivors and their final (C) result
| scenario | A avg % (t) | B avg % (t) | **C avg %** (t) | C 2x costs | C trades/day | C shorts avg % | C longs avg % |
|---|---|---|---|---|---|---|---|
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.674 (3.7) | +0.207 (3.3) | **-0.131** (-3.7) | -0.261 | 3.6 | -0.187 | -0.046 |
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.663 (3.7) | +0.201 (3.2) | **-0.134** (-3.8) | -0.264 | 3.6 | -0.190 | -0.049 |
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.663 (3.7) | +0.201 (3.2) | **-0.134** (-3.8) | -0.264 | 3.6 | -0.190 | -0.049 |
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.663 (3.7) | +0.201 (3.2) | **-0.134** (-3.7) | -0.264 | 3.6 | -0.190 | -0.048 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.624 (3.7) | +0.183 (3.0) | **-0.127** (-3.6) | -0.257 | 3.7 | -0.180 | -0.044 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.703 (3.6) | +0.211 (3.0) | **-0.119** (-3.0) | -0.249 | 3.3 | -0.194 | -0.003 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.691 (3.6) | +0.205 (3.0) | **-0.122** (-3.1) | -0.252 | 3.3 | -0.197 | -0.006 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.691 (3.6) | +0.205 (3.0) | **-0.122** (-3.1) | -0.252 | 3.3 | -0.197 | -0.006 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.691 (3.6) | +0.205 (3.0) | **-0.122** (-3.1) | -0.252 | 3.3 | -0.197 | -0.005 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.613 (3.6) | +0.177 (2.9) | **-0.131** (-3.7) | -0.261 | 3.7 | -0.184 | -0.048 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.613 (3.6) | +0.177 (2.9) | **-0.131** (-3.7) | -0.261 | 3.7 | -0.184 | -0.048 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.614 (3.6) | +0.176 (2.9) | **-0.129** (-3.7) | -0.259 | 3.7 | -0.183 | -0.046 |
| 30m break 12 bars, vol 5x, follow, market, stop 1.5 ATR, TP none, trail on, hold 6 bars | +0.569 (3.4) | +0.190 (2.8) | **-0.192** (-4.7) | -0.322 | 3.7 | -0.255 | -0.094 |
| 30m break 48 bars, vol 5x, follow, market, stop 1.5 ATR, TP none, trail on, hold 6 bars | +0.641 (3.4) | +0.215 (2.8) | **-0.195** (-4.4) | -0.325 | 3.3 | -0.286 | -0.055 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.807 (3.5) | +0.237 (2.8) | **-0.146** (-3.0) | -0.276 | 2.5 | -0.247 | +0.005 |
| 30m break 24 bars, vol 5x, follow, market, stop 1.5 ATR, TP none, trail on, hold 6 bars | +0.616 (3.4) | +0.196 (2.8) | **-0.205** (-5.0) | -0.335 | 3.6 | -0.276 | -0.096 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.793 (3.4) | +0.234 (2.8) | **-0.150** (-3.1) | -0.280 | 2.5 | -0.251 | +0.001 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.793 (3.4) | +0.234 (2.8) | **-0.150** (-3.1) | -0.280 | 2.5 | -0.251 | +0.001 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.396 (2.8) | +0.241 (2.8) | **-0.084** (-2.0) | -0.164 | 2.9 | -0.063 | -0.118 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.793 (3.4) | +0.233 (2.8) | **-0.150** (-3.1) | -0.280 | 2.5 | -0.251 | +0.003 |
| 15m break 192 bars, vol 5x, follow, market, stop 3 ATR, TP 1R, trail off, hold 12 bars | +0.253 (4.0) | +0.157 (2.8) | **-0.213** (-4.2) | -0.328 | 4.2 | -0.232 | -0.183 |
| 30m break 48 bars, vol 5x, follow, market, stop 2 ATR, TP none, trail on, hold 6 bars | +0.564 (3.0) | +0.224 (2.7) | **-0.284** (-5.8) | -0.414 | 3.3 | -0.391 | -0.119 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 48 bars | +0.391 (2.8) | +0.238 (2.7) | **-0.092** (-2.2) | -0.172 | 2.9 | -0.070 | -0.129 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 144 bars | +0.391 (2.8) | +0.238 (2.7) | **-0.092** (-2.2) | -0.172 | 2.9 | -0.070 | -0.129 |
| 30m break 24 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 48 bars | +0.386 (2.9) | +0.214 (2.7) | **-0.101** (-2.7) | -0.181 | 3.1 | -0.071 | -0.152 |
| 30m break 24 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 144 bars | +0.386 (2.9) | +0.214 (2.7) | **-0.101** (-2.7) | -0.181 | 3.1 | -0.071 | -0.152 |
| 30m break 12 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.359 (2.9) | +0.200 (2.7) | **-0.084** (-2.2) | -0.164 | 3.2 | -0.047 | -0.144 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 12 bars | +0.392 (2.8) | +0.235 (2.7) | **-0.092** (-2.2) | -0.172 | 2.9 | -0.070 | -0.128 |
| 30m break 24 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.390 (3.0) | +0.211 (2.7) | **-0.093** (-2.5) | -0.173 | 3.1 | -0.064 | -0.141 |
| 30m break 12 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 48 bars | +0.360 (2.9) | +0.199 (2.7) | **-0.091** (-2.4) | -0.171 | 3.2 | -0.053 | -0.155 |

## What picking the best-looking (A only) would have done
| scenario | A avg % | C avg % |
|---|---|---|
| 60m break 96 bars, vol 5x, follow, limit, stop 3 ATR, TP 3R, trail off, hold 144 bars | +1.760 | +0.128 |
| 60m break 192 bars, vol 5x, follow, limit, stop 3 ATR, TP none, trail on, hold 144 bars | +1.709 | +0.100 |
| 60m break 96 bars, vol 5x, follow, limit, stop 3 ATR, TP none, trail on, hold 144 bars | +1.701 | +0.284 |
| 30m break 288 bars, vol 5x, follow, market, stop 3 ATR, TP none, trail on, hold 144 bars | +1.658 | -0.459 |
| 30m break 288 bars, vol 5x, follow, market, stop 3 ATR, TP none, trail on, hold 48 bars | +1.625 | -0.508 |

Per trade % is of the position. At 30% of the account x 10x, account % per trade = 3x that.
