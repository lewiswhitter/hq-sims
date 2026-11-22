# Big-move scenario farm (115,200 scenarios, 10 coins, 751 days of 1m data)

**Verdict:** NO RELIABLE EDGE: 129 scenarios passed the pick + confirm periods (~61 by luck; similar scenarios share trades so they pass in clusters), and 0 held up in the newest period.

- Scenarios tested: 115,200; with enough trades in every period: 115,200
- Up with t>=2 in A (oldest half, pick): 4,107
- ...and in B (next quarter, confirm): 129 (luck alone ~61, rough: scenarios share trades)
- ...and in C (newest quarter, final): 0
- Costs: taker 0.045% + 0.02% slippage per market fill, maker 0.015%. 'C 2x' = C with costs doubled.

Where the A+B survivors came from: bar: {1: 0, 15: 29, 3: 0, 30: 86, 5: 0, 60: 14}; mode: {'fade': 0, 'follow': 129}; entry: {'limit': 45, 'market': 84}; vol: {0: 0, 1.5: 0, 2: 4, 3: 2, 5: 123}

## Top 30 A+B survivors and their final (C) result
| scenario | A avg % (t) | B avg % (t) | **C avg %** (t) | C 2x costs | C trades/day | C shorts avg % | C longs avg % |
|---|---|---|---|---|---|---|---|
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.670 (3.7) | +0.200 (3.2) | **-0.116** (-3.2) | -0.246 | 3.5 | -0.161 | -0.046 |
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.659 (3.7) | +0.194 (3.1) | **-0.119** (-3.3) | -0.249 | 3.5 | -0.164 | -0.049 |
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.659 (3.7) | +0.194 (3.1) | **-0.119** (-3.3) | -0.249 | 3.5 | -0.164 | -0.049 |
| 30m break 24 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.659 (3.7) | +0.194 (3.1) | **-0.119** (-3.3) | -0.249 | 3.5 | -0.164 | -0.048 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.620 (3.6) | +0.177 (3.0) | **-0.113** (-3.2) | -0.243 | 3.6 | -0.156 | -0.048 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.699 (3.6) | +0.202 (3.0) | **-0.110** (-2.7) | -0.240 | 3.2 | -0.179 | -0.004 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.687 (3.6) | +0.196 (2.9) | **-0.113** (-2.8) | -0.243 | 3.2 | -0.182 | -0.007 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.687 (3.6) | +0.196 (2.9) | **-0.113** (-2.8) | -0.243 | 3.2 | -0.182 | -0.007 |
| 30m break 48 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.688 (3.6) | +0.196 (2.9) | **-0.112** (-2.8) | -0.242 | 3.2 | -0.182 | -0.006 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.610 (3.6) | +0.170 (2.9) | **-0.117** (-3.3) | -0.247 | 3.6 | -0.160 | -0.051 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.610 (3.6) | +0.170 (2.9) | **-0.117** (-3.3) | -0.247 | 3.6 | -0.160 | -0.051 |
| 30m break 12 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.610 (3.6) | +0.169 (2.9) | **-0.115** (-3.2) | -0.245 | 3.6 | -0.158 | -0.050 |
| 30m break 12 bars, vol 5x, follow, market, stop 1.5 ATR, TP none, trail on, hold 6 bars | +0.564 (3.3) | +0.183 (2.8) | **-0.179** (-4.4) | -0.309 | 3.6 | -0.231 | -0.100 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.393 (2.8) | +0.238 (2.8) | **-0.065** (-1.5) | -0.145 | 2.8 | -0.028 | -0.126 |
| 30m break 48 bars, vol 5x, follow, market, stop 1.5 ATR, TP none, trail on, hold 6 bars | +0.637 (3.3) | +0.206 (2.8) | **-0.187** (-4.1) | -0.317 | 3.2 | -0.272 | -0.058 |
| 30m break 24 bars, vol 5x, follow, market, stop 1.5 ATR, TP none, trail on, hold 6 bars | +0.611 (3.4) | +0.189 (2.8) | **-0.191** (-4.6) | -0.321 | 3.5 | -0.251 | -0.098 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 6 bars | +0.805 (3.5) | +0.226 (2.8) | **-0.133** (-2.7) | -0.263 | 2.5 | -0.227 | +0.008 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 48 bars | +0.388 (2.8) | +0.235 (2.7) | **-0.073** (-1.7) | -0.153 | 2.8 | -0.035 | -0.137 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 144 bars | +0.388 (2.8) | +0.235 (2.7) | **-0.073** (-1.7) | -0.153 | 2.8 | -0.035 | -0.137 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 48 bars | +0.791 (3.4) | +0.223 (2.7) | **-0.137** (-2.8) | -0.267 | 2.5 | -0.231 | +0.004 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 144 bars | +0.791 (3.4) | +0.223 (2.7) | **-0.137** (-2.8) | -0.267 | 2.5 | -0.231 | +0.004 |
| 30m break 96 bars, vol 5x, follow, market, stop 1 ATR, TP none, trail on, hold 12 bars | +0.791 (3.4) | +0.222 (2.7) | **-0.136** (-2.8) | -0.266 | 2.5 | -0.231 | +0.006 |
| 30m break 24 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 48 bars | +0.383 (2.9) | +0.211 (2.7) | **-0.075** (-1.9) | -0.155 | 3.1 | -0.024 | -0.159 |
| 30m break 24 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 144 bars | +0.383 (2.9) | +0.211 (2.7) | **-0.075** (-1.9) | -0.155 | 3.1 | -0.024 | -0.159 |
| 30m break 48 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 12 bars | +0.389 (2.8) | +0.232 (2.7) | **-0.073** (-1.7) | -0.153 | 2.8 | -0.035 | -0.135 |
| 30m break 12 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.357 (2.9) | +0.198 (2.7) | **-0.059** (-1.5) | -0.139 | 3.2 | -0.002 | -0.154 |
| 30m break 24 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.387 (3.0) | +0.208 (2.7) | **-0.067** (-1.7) | -0.147 | 3.1 | -0.018 | -0.148 |
| 30m break 12 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 48 bars | +0.358 (2.9) | +0.197 (2.7) | **-0.067** (-1.7) | -0.147 | 3.2 | -0.008 | -0.164 |
| 30m break 12 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 144 bars | +0.358 (2.9) | +0.197 (2.7) | **-0.067** (-1.7) | -0.147 | 3.2 | -0.008 | -0.164 |
| 30m break 96 bars, vol 5x, follow, limit, stop 1 ATR, TP none, trail on, hold 6 bars | +0.487 (3.0) | +0.279 (2.7) | **-0.118** (-2.3) | -0.198 | 2.2 | -0.114 | -0.123 |

## What picking the best-looking (A only) would have done
| scenario | A avg % | C avg % |
|---|---|---|
| 60m break 96 bars, vol 5x, follow, limit, stop 3 ATR, TP 3R, trail off, hold 144 bars | +1.760 | +0.315 |
| 60m break 192 bars, vol 5x, follow, limit, stop 3 ATR, TP none, trail on, hold 144 bars | +1.709 | +0.116 |
| 60m break 96 bars, vol 5x, follow, limit, stop 3 ATR, TP none, trail on, hold 144 bars | +1.701 | +0.293 |
| 30m break 288 bars, vol 5x, follow, market, stop 3 ATR, TP none, trail on, hold 144 bars | +1.658 | -0.448 |
| 30m break 288 bars, vol 5x, follow, market, stop 3 ATR, TP none, trail on, hold 48 bars | +1.625 | -0.511 |

Per trade % is of the position. At 30% of the account x 10x, account % per trade = 3x that.
