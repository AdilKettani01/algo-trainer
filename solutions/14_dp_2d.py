"""Section 14 - Dynamic Programming II: grids, strings, knapsack, state machines (reference solutions)."""
from math import inf
from typing import List


def unique_paths(m: int, n: int) -> int:
    """Robot on an m x n grid moves only right/down from top-left to bottom-right. Number of paths?

    unique_paths(3, 7) -> 28
    Target: O(m*n), O(n) space. dp[r][c] = dp[r-1][c] + dp[r][c-1].
    """
    row = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]
    return row[-1]


def min_path_sum(grid: List[List[int]]) -> int:
    """Min sum path from top-left to bottom-right moving only right/down.

    min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) -> 7
    Target: O(R*C).
    """
    R, C = len(grid), len(grid[0])
    dp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if r == c == 0:
                dp[r][c] = grid[0][0]
            else:
                dp[r][c] = grid[r][c] + min(dp[r - 1][c] if r else inf, dp[r][c - 1] if c else inf)
    return dp[-1][-1]


def longest_common_subsequence(a: str, b: str) -> int:
    """Length of the longest subsequence (not necessarily contiguous) common to a and b.

    longest_common_subsequence("abcde", "ace") -> 3
    Target: O(len(a) * len(b)).
    """
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def min_distance(a: str, b: str) -> int:
    """Edit distance: min insert/delete/replace operations to turn a into b.

    min_distance("horse", "ros") -> 3
    Target: O(len(a) * len(b)).
    """
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[-1][-1]


def can_partition(nums: List[int]) -> bool:
    """Can nums be split into two subsets with equal sum?

    can_partition([1,5,11,5]) -> True
    Target: subset-sum DP. Python trick: use an int as a bitset.
    """
    total = sum(nums)
    if total % 2:
        return False
    target, bits = total // 2, 1  # bit i set <=> sum i reachable
    for x in nums:
        bits |= bits << x
    return bool(bits >> target & 1)


def coin_change_ways(amount: int, coins: List[int]) -> int:
    """Number of COMBINATIONS (order ignored) of coins that make `amount`.

    coin_change_ways(5, [1,2,5]) -> 4
    Target: O(amount * coins). Loop coins on the OUTSIDE to avoid counting permutations.
    """
    dp = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """Classic 0/1 knapsack: max total value without exceeding capacity (each item at most once).

    knapsack_01([1,3,4,5], [1,4,5,7], 7) -> 9
    Target: O(n * capacity). Iterate capacity DOWNWARD when using a 1D array.
    """
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for cap in range(capacity, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[capacity]


def max_profit_cooldown(prices: List[int]) -> int:
    """Buy/sell stock many times, but after selling you must rest one day. Max profit.

    max_profit_cooldown([1,2,3,0,2]) -> 3
    Target: O(n). State machine: hold / sold / rest.
    """
    hold, sold, rest = -inf, 0, 0
    for p in prices:
        prev_sold = sold
        sold = hold + p
        hold = max(hold, rest - p)
        rest = max(rest, prev_sold)
    return max(sold, rest)
