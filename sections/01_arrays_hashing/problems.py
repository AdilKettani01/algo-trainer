'Section 01 - Arrays & Hashing (your workspace).'


from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices [i, j] (i != j) such that nums[i] + nums[j] == target.
    Exactly one valid pair exists.

    two_sum([2, 7, 11, 15], 9) -> [0, 1]
    Target: O(n) time, O(n) space.
    """
    pass


def contains_duplicate(nums: List[int]) -> bool:
    """Return True if any value appears at least twice.

    contains_duplicate([1, 2, 3, 1]) -> True
    Target: O(n) time.
    """
    pass


def is_anagram(s: str, t: str) -> bool:
    """Return True if t is a rearrangement of s.

    is_anagram("anagram", "nagaram") -> True
    Target: O(n) time.
    """
    pass


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group words that are anagrams of each other (any group order).

    group_anagrams(["eat","tea","tan","ate","nat","bat"])
      -> [["eat","tea","ate"],["tan","nat"],["bat"]]
    Target: O(n * k log k) where k = longest word.
    """
    pass


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Return the k most frequent values (any order).

    top_k_frequent([1,1,1,2,2,3], 2) -> [1, 2]
    Target: O(n) with bucket sort (O(n log k) with a heap is fine too).
    """
    pass


def product_except_self(nums: List[int]) -> List[int]:
    """out[i] = product of every element except nums[i]. No division allowed.

    product_except_self([1,2,3,4]) -> [24,12,8,6]
    Target: O(n) time, O(1) extra space (besides output).
    """
    pass


def longest_consecutive(nums: List[int]) -> int:
    """Length of the longest run of consecutive integers (order in nums irrelevant).

    longest_consecutive([100,4,200,1,3,2]) -> 4   (1,2,3,4)
    Target: O(n) time.
    """
    pass
