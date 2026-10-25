'Section 13 - Dynamic Programming I: one dimension (your workspace).'


from typing import List


def climb_stairs(n: int) -> int:
    """Ways to climb n stairs taking 1 or 2 steps at a time.

    climb_stairs(3) -> 3
    Target: O(n) time, O(1) space. dp[i] = dp[i-1] + dp[i-2].
    """
    pass


def rob(nums: List[int]) -> int:
    """Max money robbing houses in a line without robbing two adjacent houses.

    rob([2,7,9,3,1]) -> 12
    Target: O(n). dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
    """
    pass


def rob_circular(nums: List[int]) -> int:
    """Same as rob, but the houses form a CIRCLE (first and last are adjacent).

    rob_circular([2,3,2]) -> 3
    Target: O(n). Run rob twice: without the first house, then without the last.
    """
    pass


def coin_change(coins: List[int], amount: int) -> int:
    """Fewest coins (unlimited supply of each) that make `amount`; -1 if impossible.

    coin_change([1,2,5], 11) -> 3
    Target: O(amount * len(coins)).
    """
    pass


def length_of_lis(nums: List[int]) -> int:
    """Length of the longest STRICTLY increasing subsequence.

    length_of_lis([10,9,2,5,3,7,101,18]) -> 4
    Target: O(n log n) with 'patience sorting' + binary search (O(n^2) DP is the stepping stone).
    """
    pass


def word_break(s: str, word_dict: List[str]) -> bool:
    """Can s be split into a sequence of words from word_dict (words reusable)?

    word_break("leetcode", ["leet","code"]) -> True
    Target: O(n * maxwordlen). dp[i] = can s[:i] be built?
    """
    pass


def num_decodings(s: str) -> int:
    """'A'->1 ... 'Z'->26. Number of ways to decode a digit string (0 if impossible).

    num_decodings("226") -> 3   ("BZ", "VF", "BBF")
    Target: O(n).
    """
    pass


def max_product_subarray(nums: List[int]) -> int:
    """Largest product of a contiguous subarray.

    max_product_subarray([2,3,-2,4]) -> 6
    Target: O(n). Track BOTH the max and min product ending here (a negative flips them).
    """
    pass
