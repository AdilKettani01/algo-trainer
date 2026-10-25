'Section 04 - Prefix Sums & Intervals (your workspace).'


from typing import List


class NumArray:
    """Immutable array with fast range-sum queries.

    NumArray([-2,0,3,-5,2,-1]).sum_range(0, 2) -> 1   (inclusive both ends)
    Target: O(n) build, O(1) per query.
    """

    def __init__(self, nums: List[int]):
        pass

    def sum_range(self, left: int, right: int) -> int:
        """Sum of nums[left..right] inclusive."""
        pass


def subarray_sum(nums: List[int], k: int) -> int:
    """Count contiguous subarrays whose sum equals k (values may be negative).

    subarray_sum([1,2,3], 3) -> 2   ([1,2] and [3])
    Target: O(n) time with a hash map of prefix sums.
    """
    pass


def find_max_length(nums: List[int]) -> int:
    """Longest contiguous subarray of a 0/1 array with equal numbers of 0s and 1s.

    find_max_length([0,1,0]) -> 2
    Target: O(n). Hint: treat 0 as -1, then it's 'longest subarray with sum 0'.
    """
    pass


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """Merge all overlapping intervals (touching counts as overlapping).

    merge([[1,3],[2,6],[8,10],[15,18]]) -> [[1,6],[8,10],[15,18]]
    Target: O(n log n).
    """
    pass


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """Minimum number of rooms needed so no two overlapping meetings share one.
    A meeting ending at t does not conflict with one starting at t.

    min_meeting_rooms([[0,30],[5,10],[15,20]]) -> 2
    Target: O(n log n) - sweep line over sorted starts and ends.
    """
    pass
