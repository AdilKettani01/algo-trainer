'Section 09 - Heaps / Priority Queues (your workspace).'


from typing import List, Optional


from helpers import ListNode


def find_kth_largest(nums: List[int], k: int) -> int:
    """k-th largest element (1-indexed) of an unsorted array.

    find_kth_largest([3,2,1,5,6,4], 2) -> 5
    Target: O(n log k) with a size-k min-heap.
    """
    pass


def last_stone_weight(stones: List[int]) -> int:
    """Repeatedly smash the two heaviest stones (y>=x): x destroyed; y becomes y-x. Return last weight (0 if none).

    last_stone_weight([2,7,4,1,8,1]) -> 1
    Target: O(n log n). Python only has a MIN-heap: store negatives.
    """
    pass


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """k points closest to the origin (any order). Compare squared distances.

    k_closest([[1,3],[-2,2]], 1) -> [[-2,2]]
    Target: O(n log k).
    """
    pass


class MedianFinder:
    """Stream of numbers; median available at any time.

    add_num(1); add_num(2); find_median() -> 1.5
    Target: O(log n) add, O(1) find. Hint: max-heap (lower half) + min-heap (upper half).
    """

    def __init__(self):
        pass

    def add_num(self, num: int) -> None:
        pass

    def find_median(self) -> float:
        pass


def least_interval(tasks: List[str], n: int) -> int:
    """CPU runs one task per unit time; the same task needs n units of cooldown. Min total time (idle allowed).

    least_interval(["A","A","A","B","B","B"], 2) -> 8
    Target: O(T). Greedy: always run the task with the most remaining count.
    """
    pass


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted linked lists into one sorted list.

    Target: O(N log k). Heap holds the current head of each list.
    """
    pass
