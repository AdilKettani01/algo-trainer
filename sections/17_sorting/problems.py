'Section 17 - Sorting & Selection (your workspace).'


from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    """Return a NEW sorted list using merge sort. Don't use sorted()/list.sort().

    Target: O(n log n) always, stable, O(n) extra space.
    """
    pass


def quick_sort(nums: List[int]) -> List[int]:
    """Return a NEW sorted list using quicksort with a random pivot. Must handle many duplicates.

    Target: O(n log n) expected. (Partition into <, ==, > pivot.)
    """
    pass


def heap_sort(nums: List[int]) -> List[int]:
    """Return a NEW sorted list using heap sort. Build your own heap (don't import heapq).

    Target: O(n log n), O(1) extra space beyond the copy.
    """
    pass


def quickselect(nums: List[int], k: int) -> int:
    """k-th SMALLEST element (1-indexed) without fully sorting.

    quickselect([7,10,4,3,20,15], 3) -> 7
    Target: O(n) expected.
    """
    pass


def sort_colors(nums: List[int]) -> None:
    """Sort an array containing only 0, 1, 2 IN PLACE in one pass (Dutch national flag).

    [2,0,2,1,1,0] becomes [0,0,1,1,2,2]
    Target: O(n) time, O(1) space.
    """
    pass


def count_inversions(nums: List[int]) -> int:
    """Number of pairs i < j with nums[i] > nums[j].

    count_inversions([2,4,1,3,5]) -> 3
    Target: O(n log n). Count while merging in merge sort.
    """
    pass
