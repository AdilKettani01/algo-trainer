"""Section 01 - Arrays & Hashing (reference solutions)."""
from collections import Counter, defaultdict
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices [i, j] (i != j) such that nums[i] + nums[j] == target.
    Exactly one valid pair exists.

    two_sum([2, 7, 11, 15], 9) -> [0, 1]
    Target: O(n) time, O(n) space.
    """
    seen = {}  # value -> index where we saw it
    for i, x in enumerate(nums):
        if target - x in seen:  # complement already seen?
            return [seen[target - x], i]
        seen[x] = i


def contains_duplicate(nums: List[int]) -> bool:
    """Return True if any value appears at least twice.

    contains_duplicate([1, 2, 3, 1]) -> True
    Target: O(n) time.
    """
    return len(set(nums)) < len(nums)


def is_anagram(s: str, t: str) -> bool:
    """Return True if t is a rearrangement of s.

    is_anagram("anagram", "nagaram") -> True
    Target: O(n) time.
    """
    return Counter(s) == Counter(t)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group words that are anagrams of each other (any group order).

    group_anagrams(["eat","tea","tan","ate","nat","bat"])
      -> [["eat","tea","ate"],["tan","nat"],["bat"]]
    Target: O(n * k log k) where k = longest word.
    """
    groups = defaultdict(list)
    for w in strs:
        groups[tuple(sorted(w))].append(w)  # sorted letters = canonical key
    return list(groups.values())


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Return the k most frequent values (any order).

    top_k_frequent([1,1,1,2,2,3], 2) -> [1, 2]
    Target: O(n) with bucket sort (O(n log k) with a heap is fine too).
    """
    buckets = [[] for _ in range(len(nums) + 1)]  # index = frequency
    for val, freq in Counter(nums).items():
        buckets[freq].append(val)
    out = []
    for freq in range(len(buckets) - 1, 0, -1):
        for val in buckets[freq]:
            out.append(val)
            if len(out) == k:
                return out


def product_except_self(nums: List[int]) -> List[int]:
    """out[i] = product of every element except nums[i]. No division allowed.

    product_except_self([1,2,3,4]) -> [24,12,8,6]
    Target: O(n) time, O(1) extra space (besides output).
    """
    n = len(nums)
    out = [1] * n
    prefix = 1
    for i in range(n):  # out[i] = product of everything to the LEFT
        out[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):  # multiply by everything to the RIGHT
        out[i] *= suffix
        suffix *= nums[i]
    return out


def longest_consecutive(nums: List[int]) -> int:
    """Length of the longest run of consecutive integers (order in nums irrelevant).

    longest_consecutive([100,4,200,1,3,2]) -> 4   (1,2,3,4)
    Target: O(n) time.
    """
    s, best = set(nums), 0
    for x in s:
        if x - 1 not in s:  # only start counting at the beginning of a run
            length = 1
            while x + length in s:
                length += 1
            best = max(best, length)
    return best
