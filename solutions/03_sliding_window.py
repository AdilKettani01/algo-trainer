"""Section 03 - Sliding Window (reference solutions)."""
from collections import Counter
from math import inf
from typing import List


def max_sum_subarray(nums: List[int], k: int) -> int:
    """Max sum of any contiguous subarray of exactly length k.

    max_sum_subarray([2,1,5,1,3,2], 3) -> 9
    Target: O(n) time (fixed-size window).
    """
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]  # slide: add right, drop left
        best = max(best, window)
    return best


def length_of_longest_substring(s: str) -> int:
    """Length of the longest substring without repeating characters.

    length_of_longest_substring("abcabcbb") -> 3
    Target: O(n) time.
    """
    last, l, best = {}, 0, 0
    for r, ch in enumerate(s):
        if ch in last and last[ch] >= l:
            l = last[ch] + 1  # jump left edge past the previous copy
        last[ch] = r
        best = max(best, r - l + 1)
    return best


def min_subarray_len(target: int, nums: List[int]) -> int:
    """Length of the shortest contiguous subarray with sum >= target (all nums > 0); 0 if none.

    min_subarray_len(7, [2,3,1,2,4,3]) -> 2
    Target: O(n) time (variable window).
    """
    l = total = 0
    best = inf
    for r, x in enumerate(nums):
        total += x
        while total >= target:  # shrink while still valid
            best = min(best, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if best == inf else best


def character_replacement(s: str, k: int) -> int:
    """Longest substring you can make all one letter using at most k replacements.

    character_replacement("AABABBA", 1) -> 4
    Target: O(n) time.
    """
    count, l, maxf, best = Counter(), 0, 0, 0
    for r, ch in enumerate(s):
        count[ch] += 1
        maxf = max(maxf, count[ch])  # most frequent letter seen in any window
        while (r - l + 1) - maxf > k:  # letters to replace > k -> shrink
            count[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best


def min_window(s: str, t: str) -> str:
    """Smallest substring of s containing every character of t (with multiplicity); "" if none.

    min_window("ADOBECODEBANC", "ABC") -> "BANC"
    Target: O(len(s) + len(t)).
    """
    if not t or len(t) > len(s):
        return ""
    need, missing, l = Counter(t), len(t), 0
    best = (inf, 0, 0)
    for r, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:  # window valid: shrink from the left
            while need[s[l]] < 0:
                need[s[l]] += 1
                l += 1
            if r - l + 1 < best[0]:
                best = (r - l + 1, l, r + 1)
            need[s[l]] += 1  # drop s[l] -> window invalid again
            missing += 1
            l += 1
    return "" if best[0] == inf else s[best[1]:best[2]]
