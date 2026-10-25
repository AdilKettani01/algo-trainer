# 13 - Dynamic Programming I (1-D)

## What is DP?
Recursion with **overlapping subproblems** + **optimal substructure**, where you store each subproblem's answer so it's computed once. Fibonacci naive = O(2ⁿ); with memo = O(n).

## The 5-step recipe
1. **State**: what does `dp[i]` mean? (Write it in a sentence.)
2. **Transition**: how does `dp[i]` depend on smaller states?
3. **Base cases**.
4. **Order**: compute smaller states first (or use top-down memo).
5. **Answer**: which cell(s)? Then **compress space** if only the last 1-2 values are used.

## Two styles
```python
# Top-down (memo)                      # Bottom-up (table)
@lru_cache(None)                       dp = [0] * (n + 1)
def f(i): ...                          for i in range(1, n + 1): dp[i] = ...
```

## Patterns in this section
| Problem | State | Transition |
|---|---|---|
| Climbing stairs | `dp[i]` ways to reach i | `dp[i-1] + dp[i-2]` |
| House robber | best loot up to i | `max(dp[i-1], dp[i-2] + a[i])` (circular: run twice, drop first / last) |
| Coin change (min coins) | fewest coins for amount a | `min(dp[a-c] + 1)` over coins |
| Word break | can s[:i] be built | `any(dp[j] and s[j:i] in words)` |
| Decode ways | ways for s[:i] | add `dp[i-1]` if 1 digit valid, `dp[i-2]` if 2 digits in 10..26 |
| LIS | `dp[i]` = LIS ending at i (O(n²)) | `max(dp[j]+1)` for `a[j] < a[i]`; **O(n log n)**: keep `tails[]`, binary-search each value |
| Max product subarray | track max AND min ending here | negatives swap them |
| Kadane (section 15) | best sum ending at i | `max(a[i], dp[i-1] + a[i])` |

## Pitfalls
- Initialise "impossible" with a big number (`amount + 1`) and convert to `-1` at the end.
- Iterate in the right order (coins: *unbounded*, so go ascending).
- Think `dp[i]` = "ending at i" vs "using first i items" - be consistent.

**Practice:** `climb_stairs`, `rob`, `rob_circular`, `coin_change`, `length_of_lis`, `word_break`, `num_decodings`, `max_product_subarray`.
