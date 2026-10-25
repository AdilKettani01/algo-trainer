"""Section 13 - Dynamic Programming I: one dimension (reference solutions)."""
from bisect import bisect_left
from typing import List


def climb_stairs(n: int) -> int:
    """Ways to climb n stairs taking 1 or 2 steps at a time.

    climb_stairs(3) -> 3
    Target: O(n) time, O(1) space. dp[i] = dp[i-1] + dp[i-2].
    """
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def rob(nums: List[int]) -> int:
    """Max money robbing houses in a line without robbing two adjacent houses.

    rob([2,7,9,3,1]) -> 12
    Target: O(n). dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
    """
    skip, take = 0, 0
    for x in nums:
        skip, take = max(skip, take), skip + x
    return max(skip, take)


def rob_circular(nums: List[int]) -> int:
    """Same as rob, but the houses form a CIRCLE (first and last are adjacent).

    rob_circular([2,3,2]) -> 3
    Target: O(n). Run rob twice: without the first house, then without the last.
    """
    if len(nums) == 1:
        return nums[0]
    return max(rob(nums[1:]), rob(nums[:-1]))


def coin_change(coins: List[int], amount: int) -> int:
    """Fewest coins (unlimited supply of each) that make `amount`; -1 if impossible.

    coin_change([1,2,5], 11) -> 3
    Target: O(amount * len(coins)).
    """
    INF = amount + 1
    dp = [0] + [INF] * amount  # dp[a] = fewest coins for amount a
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != INF else -1


def length_of_lis(nums: List[int]) -> int:
    """Length of the longest STRICTLY increasing subsequence.

    length_of_lis([10,9,2,5,3,7,101,18]) -> 4
    Target: O(n log n) with 'patience sorting' + binary search (O(n^2) DP is the stepping stone).
    """
    tails = []  # tails[i] = smallest tail of an increasing subsequence of length i+1
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def word_break(s: str, word_dict: List[str]) -> bool:
    """Can s be split into a sequence of words from word_dict (words reusable)?

    word_break("leetcode", ["leet","code"]) -> True
    Target: O(n * maxwordlen). dp[i] = can s[:i] be built?
    """
    words = set(word_dict)
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        dp[i] = any(dp[j] and s[j:i] in words for j in range(i))
    return dp[-1]


def num_decodings(s: str) -> int:
    """'A'->1 ... 'Z'->26. Number of ways to decode a digit string (0 if impossible).

    num_decodings("226") -> 3   ("BZ", "VF", "BBF")
    Target: O(n).
    """
    prev2, prev1 = 1, 1 if s and s[0] != "0" else 0
    if not s:
        return 0
    for i in range(1, len(s)):
        cur = 0
        if s[i] != "0":
            cur += prev1
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            cur += prev2
        prev2, prev1 = prev1, cur
    return prev1


def max_product_subarray(nums: List[int]) -> int:
    """Largest product of a contiguous subarray.

    max_product_subarray([2,3,-2,4]) -> 6
    Target: O(n). Track BOTH the max and min product ending here (a negative flips them).
    """
    best = hi = lo = nums[0]
    for x in nums[1:]:
        cands = (x, hi * x, lo * x)
        hi, lo = max(cands), min(cands)
        best = max(best, hi)
    return best
