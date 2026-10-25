'Section 03 - Sliding Window (your workspace).'


from typing import List


def max_sum_subarray(nums: List[int], k: int) -> int:
    """Max sum of any contiguous subarray of exactly length k.

    max_sum_subarray([2,1,5,1,3,2], 3) -> 9
    Target: O(n) time (fixed-size window).
    """
    pass


def length_of_longest_substring(s: str) -> int:
    """Length of the longest substring without repeating characters.

    length_of_longest_substring("abcabcbb") -> 3
    Target: O(n) time.
    """
    pass


def min_subarray_len(target: int, nums: List[int]) -> int:
    """Length of the shortest contiguous subarray with sum >= target (all nums > 0); 0 if none.

    min_subarray_len(7, [2,3,1,2,4,3]) -> 2
    Target: O(n) time (variable window).
    """
    pass


def character_replacement(s: str, k: int) -> int:
    """Longest substring you can make all one letter using at most k replacements.

    character_replacement("AABABBA", 1) -> 4
    Target: O(n) time.
    """
    pass


def min_window(s: str, t: str) -> str:
    """Smallest substring of s containing every character of t (with multiplicity); "" if none.

    min_window("ADOBECODEBANC", "ABC") -> "BANC"
    Target: O(len(s) + len(t)).
    """
    pass
