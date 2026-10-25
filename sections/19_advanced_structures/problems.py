'Section 19 - Advanced Data Structures (your workspace).'


from typing import List


class LRUCache:
    """Least-Recently-Used cache with O(1) get and put.

    cache = LRUCache(2); put(1,1); put(2,2); get(1) -> 1; put(3,3) evicts key 2; get(2) -> -1
    Target: O(1) per op. (Interview classic: hash map + doubly linked list; OrderedDict does both.)
    """

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


class FenwickTree:
    """Binary Indexed Tree: point updates + prefix sums, both O(log n). 0-indexed API.

    ft = FenwickTree(5); ft.update(2, 10); ft.prefix_sum(3) -> 10 (sum of indices 0..3)
    """

    def __init__(self, n: int):
        pass

    def update(self, i: int, delta: int) -> None:
        """Add delta to position i."""
        pass

    def prefix_sum(self, i: int) -> int:
        """Sum of positions 0..i inclusive."""
        pass


class SegmentTree:
    """Range-MINIMUM queries with point updates, both O(log n).

    st = SegmentTree([5,2,8,1]); st.query_min(0, 2) -> 2 ; st.update(3, 9); st.query_min(2, 3) -> 8
    """

    def __init__(self, nums: List[int]):
        pass

    def update(self, i: int, val: int) -> None:
        """Set position i to val."""
        pass

    def query_min(self, left: int, right: int) -> int:
        """Minimum over positions left..right inclusive."""
        pass


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """Maximum of every window of size k.

    sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3) -> [3,3,5,5,6,7]
    Target: O(n) with a monotonic DEQUE of indices.
    """
    pass
