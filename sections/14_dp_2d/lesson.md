# 14 - Dynamic Programming II (2-D, knapsack, state machines)

## Grid DP
`dp[r][c]` depends on the cell above and to the left.
- Unique paths: `dp[r][c] = dp[r-1][c] + dp[r][c-1]`
- Min path sum: `grid[r][c] + min(dp[r-1][c], dp[r][c-1])`
Space: keep one row.

## Two-string DP
`dp[i][j]` = answer for the first `i` chars of `a` and first `j` chars of `b`.
- **LCS**: if `a[i-1] == b[j-1]` → `dp[i-1][j-1] + 1`, else `max(dp[i-1][j], dp[i][j-1])`.
- **Edit distance**: match → `dp[i-1][j-1]`; else `1 + min(delete, insert, replace)` = `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`. Base: `dp[i][0] = i`, `dp[0][j] = j`.

## Knapsack family
- **0/1 knapsack** (each item once): `dp[cap] = max(dp[cap], dp[cap - w] + v)`, loop **capacity downward** so an item isn't reused.
- **Subset sum / partition equal subset**: boolean knapsack. Python bitset trick: `bits |= bits << x`.
- **Unbounded** (coin change ways): loop capacity **upward**.
- **Combinations vs permutations**: loop **coins outer, amount inner** → counts combinations; swapping the loops counts ordered sequences.

## State-machine DP (stock with cooldown)
Define states (`hold`, `sold`, `rest`) and transitions between them:
```
sold = hold + price
hold = max(hold, rest - price)
rest = max(rest, prev_sold)
```
Same idea for "at most k transactions", "with fee".

## Other 2-D DP to know (not coded here)
Longest palindromic subsequence, matrix chain, interval DP (burst balloons), bitmask DP (TSP, n ≤ 20), digit DP.

## Pitfalls
- 2-D → 1-D compression: mind the loop direction.
- Index shift: `dp` is `(n+1) x (m+1)` while strings are 0-indexed, hence `a[i-1]`.
- Always test tiny inputs (`""`, 1 char).

**Practice:** `unique_paths`, `min_path_sum`, `longest_common_subsequence`, `min_distance`, `can_partition`, `coin_change_ways`, `knapsack_01`, `max_profit_cooldown`.
