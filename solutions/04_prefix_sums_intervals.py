"""Section 04 - Prefix Sums & Intervals (reference solutions)."""
from typing import List


class NumArray:
    """Immutable array with fast range-sum queries.

    NumArray([-2,0,3,-5,2,-1]).sum_range(0, 2) -> 1   (inclusive both ends)
    Target: O(n) build, O(1) per query.
    """

    def __init__(self, nums: List[int]):
        self.prefix = [0]  # prefix[i] = sum of nums[:i]
        for x in nums:
            self.prefix.append(self.prefix[-1] + x)

    def sum_range(self, left: int, right: int) -> int:
        """Sum of nums[left..right] inclusive."""
        return self.prefix[right + 1] - self.prefix[left]


def subarray_sum(nums: List[int], k: int) -> int:
    """Count contiguous subarrays whose sum equals k (values may be negative).

    subarray_sum([1,2,3], 3) -> 2   ([1,2] and [3])
    Target: O(n) time with a hash map of prefix sums.
    """
    count, running, seen = 0, 0, {0: 1}
    for x in nums:
        running += x
        count += seen.get(running - k, 0)  # earlier prefix that leaves exactly k
        seen[running] = seen.get(running, 0) + 1
    return count


def find_max_length(nums: List[int]) -> int:
    """Longest contiguous subarray of a 0/1 array with equal numbers of 0s and 1s.

    find_max_length([0,1,0]) -> 2
    Target: O(n). Hint: treat 0 as -1, then it's 'longest subarray with sum 0'.
    """
    first, running, best = {0: -1}, 0, 0
    for i, x in enumerate(nums):
        running += 1 if x else -1
        if running in first:
            best = max(best, i - first[running])
        else:
            first[running] = i
    return best


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """Merge all overlapping intervals (touching counts as overlapping).

    merge([[1,3],[2,6],[8,10],[15,18]]) -> [[1,6],[8,10],[15,18]]
    Target: O(n log n).
    """
    out = []
    for s, e in sorted(intervals):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """Minimum number of rooms needed so no two overlapping meetings share one.
    A meeting ending at t does not conflict with one starting at t.

    min_meeting_rooms([[0,30],[5,10],[15,20]]) -> 2
    Target: O(n log n) - sweep line over sorted starts and ends.
    """
    starts = sorted(s for s, _ in intervals)
    ends = sorted(e for _, e in intervals)
    rooms = j = 0
    for s in starts:
        if s >= ends[j]:  # some meeting already finished -> reuse its room
            j += 1
        else:
            rooms += 1
    return rooms
