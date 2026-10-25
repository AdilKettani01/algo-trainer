"""Section 17 - Sorting & Selection (reference solutions)."""
import random
from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    """Return a NEW sorted list using merge sort. Don't use sorted()/list.sort().

    Target: O(n log n) always, stable, O(n) extra space.
    """
    if len(nums) <= 1:
        return list(nums)
    mid = len(nums) // 2
    left, right = merge_sort(nums[:mid]), merge_sort(nums[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]


def quick_sort(nums: List[int]) -> List[int]:
    """Return a NEW sorted list using quicksort with a random pivot. Must handle many duplicates.

    Target: O(n log n) expected. (Partition into <, ==, > pivot.)
    """
    if len(nums) <= 1:
        return list(nums)
    pivot = random.choice(nums)
    return (quick_sort([x for x in nums if x < pivot])
            + [x for x in nums if x == pivot]
            + quick_sort([x for x in nums if x > pivot]))


def heap_sort(nums: List[int]) -> List[int]:
    """Return a NEW sorted list using heap sort. Build your own heap (don't import heapq).

    Target: O(n log n), O(1) extra space beyond the copy.
    """
    a, n = list(nums), len(nums)

    def sift_down(i, size):
        while True:
            l, r, big = 2 * i + 1, 2 * i + 2, i
            if l < size and a[l] > a[big]:
                big = l
            if r < size and a[r] > a[big]:
                big = r
            if big == i:
                return
            a[i], a[big] = a[big], a[i]
            i = big

    for i in range(n // 2 - 1, -1, -1):  # heapify in O(n)
        sift_down(i, n)
    for end in range(n - 1, 0, -1):  # move max to the back, shrink heap
        a[0], a[end] = a[end], a[0]
        sift_down(0, end)
    return a


def quickselect(nums: List[int], k: int) -> int:
    """k-th SMALLEST element (1-indexed) without fully sorting.

    quickselect([7,10,4,3,20,15], 3) -> 7
    Target: O(n) expected.
    """
    pivot = random.choice(nums)
    lo = [x for x in nums if x < pivot]
    eq = [x for x in nums if x == pivot]
    if k <= len(lo):
        return quickselect(lo, k)
    if k <= len(lo) + len(eq):
        return pivot
    hi = [x for x in nums if x > pivot]
    return quickselect(hi, k - len(lo) - len(eq))


def sort_colors(nums: List[int]) -> None:
    """Sort an array containing only 0, 1, 2 IN PLACE in one pass (Dutch national flag).

    [2,0,2,1,1,0] becomes [0,0,1,1,2,2]
    Target: O(n) time, O(1) space.
    """
    lo, i, hi = 0, 0, len(nums) - 1
    while i <= hi:
        if nums[i] == 0:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[hi] = nums[hi], nums[i]
            hi -= 1  # don't advance i: the swapped-in value is unchecked
        else:
            i += 1


def count_inversions(nums: List[int]) -> int:
    """Number of pairs i < j with nums[i] > nums[j].

    count_inversions([2,4,1,3,5]) -> 3
    Target: O(n log n). Count while merging in merge sort.
    """
    def sort(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, cl = sort(a[:mid])
        right, cr = sort(a[mid:])
        out, i, j, cross = [], 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1
                cross += len(left) - i  # right[j] jumps over all remaining left items
        return out + left[i:] + right[j:], cl + cr + cross

    return sort(list(nums))[1]
