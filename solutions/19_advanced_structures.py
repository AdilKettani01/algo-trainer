"""Section 19 - Advanced Data Structures (reference solutions)."""
from collections import OrderedDict, deque
from math import inf
from typing import List


class LRUCache:
    """Least-Recently-Used cache with O(1) get and put.

    cache = LRUCache(2); put(1,1); put(2,2); get(1) -> 1; put(3,3) evicts key 2; get(2) -> -1
    Target: O(1) per op. (Interview classic: hash map + doubly linked list; OrderedDict does both.)
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.d.move_to_end(key)  # mark as most recently used
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        self.d.move_to_end(key)
        if len(self.d) > self.cap:
            self.d.popitem(last=False)  # evict least recently used


class FenwickTree:
    """Binary Indexed Tree: point updates + prefix sums, both O(log n). 0-indexed API.

    ft = FenwickTree(5); ft.update(2, 10); ft.prefix_sum(3) -> 10 (sum of indices 0..3)
    """

    def __init__(self, n: int):
        self.n = n
        self.t = [0] * (n + 1)

    def update(self, i: int, delta: int) -> None:
        """Add delta to position i."""
        i += 1
        while i <= self.n:
            self.t[i] += delta
            i += i & -i  # jump to the next node that covers i

    def prefix_sum(self, i: int) -> int:
        """Sum of positions 0..i inclusive."""
        i += 1
        total = 0
        while i > 0:
            total += self.t[i]
            i -= i & -i  # strip the lowest set bit
        return total


class SegmentTree:
    """Range-MINIMUM queries with point updates, both O(log n).

    st = SegmentTree([5,2,8,1]); st.query_min(0, 2) -> 2 ; st.update(3, 9); st.query_min(2, 3) -> 8
    """

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.t = [inf] * self.n + list(nums)  # leaves live at t[n:]
        for i in range(self.n - 1, 0, -1):
            self.t[i] = min(self.t[2 * i], self.t[2 * i + 1])

    def update(self, i: int, val: int) -> None:
        """Set position i to val."""
        i += self.n
        self.t[i] = val
        while i > 1:
            i //= 2
            self.t[i] = min(self.t[2 * i], self.t[2 * i + 1])

    def query_min(self, left: int, right: int) -> int:
        """Minimum over positions left..right inclusive."""
        l, r, res = left + self.n, right + self.n + 1, inf
        while l < r:
            if l & 1:
                res = min(res, self.t[l]); l += 1
            if r & 1:
                r -= 1; res = min(res, self.t[r])
            l //= 2
            r //= 2
        return res


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """Maximum of every window of size k.

    sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3) -> [3,3,5,5,6,7]
    Target: O(n) with a monotonic DEQUE of indices.
    """
    dq, out = deque(), []  # indices; values decreasing front -> back
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:  # front fell out of the window
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
