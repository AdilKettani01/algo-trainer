"""Section 06 - Binary Search (reference solutions)."""
from typing import List


def search(nums: List[int], target: int) -> int:
    """Sorted ascending, distinct. Return index of target or -1.

    search([-1,0,3,5,9,12], 9) -> 4
    Target: O(log n).
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def search_insert(nums: List[int], target: int) -> int:
    """Sorted distinct array. Return index of target, or where it would be inserted.
    (This is 'lower bound': first index with nums[i] >= target.)

    search_insert([1,3,5,6], 2) -> 1
    Target: O(log n).
    """
    lo, hi = 0, len(nums)  # hi is exclusive: answer can be len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_rotated(nums: List[int], target: int) -> int:
    """Sorted array rotated at an unknown pivot, distinct values. Index of target or -1.

    search_rotated([4,5,6,7,0,1,2], 0) -> 4
    Target: O(log n). One half is always sorted - decide which.
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def find_min(nums: List[int]) -> int:
    """Minimum of a rotated sorted array (distinct values).

    find_min([3,4,5,1,2]) -> 1
    Target: O(log n).
    """
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:  # min is to the right of mid
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


def min_eating_speed(piles: List[int], h: int) -> int:
    """Koko eats k bananas/hour from ONE pile per hour. Smallest integer k so she finishes in <= h hours.

    min_eating_speed([3,6,7,11], 8) -> 4
    Target: O(n log max(piles)). Binary search on the ANSWER.
    """
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum(-(-p // mid) for p in piles)  # ceil(p / mid)
        if hours <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo


def my_sqrt(x: int) -> int:
    """Integer square root (floor) without using ** or math.sqrt.

    my_sqrt(8) -> 2
    Target: O(log x).
    """
    lo, hi = 0, x
    while lo < hi:
        mid = (lo + hi + 1) // 2  # upper mid avoids infinite loop
        if mid * mid <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo
