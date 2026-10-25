'Section 14 - Dynamic Programming II: grids, strings, knapsack, state machines (your workspace).'


from typing import List


def unique_paths(m: int, n: int) -> int:
    """Robot on an m x n grid moves only right/down from top-left to bottom-right. Number of paths?

    unique_paths(3, 7) -> 28
    Target: O(m*n), O(n) space. dp[r][c] = dp[r-1][c] + dp[r][c-1].
    """
    pass


def min_path_sum(grid: List[List[int]]) -> int:
    """Min sum path from top-left to bottom-right moving only right/down.

    min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) -> 7
    Target: O(R*C).
    """
    pass


def longest_common_subsequence(a: str, b: str) -> int:
    """Length of the longest subsequence (not necessarily contiguous) common to a and b.

    longest_common_subsequence("abcde", "ace") -> 3
    Target: O(len(a) * len(b)).
    """
    pass


def min_distance(a: str, b: str) -> int:
    """Edit distance: min insert/delete/replace operations to turn a into b.

    min_distance("horse", "ros") -> 3
    Target: O(len(a) * len(b)).
    """
    pass


def can_partition(nums: List[int]) -> bool:
    """Can nums be split into two subsets with equal sum?

    can_partition([1,5,11,5]) -> True
    Target: subset-sum DP. Python trick: use an int as a bitset.
    """
    pass


def coin_change_ways(amount: int, coins: List[int]) -> int:
    """Number of COMBINATIONS (order ignored) of coins that make `amount`.

    coin_change_ways(5, [1,2,5]) -> 4
    Target: O(amount * coins). Loop coins on the OUTSIDE to avoid counting permutations.
    """
    pass


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """Classic 0/1 knapsack: max total value without exceeding capacity (each item at most once).

    knapsack_01([1,3,4,5], [1,4,5,7], 7) -> 9
    Target: O(n * capacity). Iterate capacity DOWNWARD when using a 1D array.
    """
    pass


def max_profit_cooldown(prices: List[int]) -> int:
    """Buy/sell stock many times, but after selling you must rest one day. Max profit.

    max_profit_cooldown([1,2,3,0,2]) -> 3
    Target: O(n). State machine: hold / sold / rest.
    """
    pass
