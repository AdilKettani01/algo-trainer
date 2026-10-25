"""Section 09 - Heaps / Priority Queues (reference solutions)."""
import heapq
from collections import Counter, deque
from typing import List, Optional

from helpers import ListNode


def find_kth_largest(nums: List[int], k: int) -> int:
    """k-th largest element (1-indexed) of an unsorted array.

    find_kth_largest([3,2,1,5,6,4], 2) -> 5
    Target: O(n log k) with a size-k min-heap.
    """
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)  # evict the smallest; heap keeps the k largest
    return heap[0]


def last_stone_weight(stones: List[int]) -> int:
    """Repeatedly smash the two heaviest stones (y>=x): x destroyed; y becomes y-x. Return last weight (0 if none).

    last_stone_weight([2,7,4,1,8,1]) -> 1
    Target: O(n log n). Python only has a MIN-heap: store negatives.
    """
    h = [-s for s in stones]
    heapq.heapify(h)
    while len(h) > 1:
        a, b = -heapq.heappop(h), -heapq.heappop(h)
        if a != b:
            heapq.heappush(h, -(a - b))
    return -h[0] if h else 0


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """k points closest to the origin (any order). Compare squared distances.

    k_closest([[1,3],[-2,2]], 1) -> [[-2,2]]
    Target: O(n log k).
    """
    return heapq.nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)


class MedianFinder:
    """Stream of numbers; median available at any time.

    add_num(1); add_num(2); find_median() -> 1.5
    Target: O(log n) add, O(1) find. Hint: max-heap (lower half) + min-heap (upper half).
    """

    def __init__(self):
        self.lo = []  # max-heap (negated) - smaller half
        self.hi = []  # min-heap - larger half

    def add_num(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))  # balance through the top
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2


def least_interval(tasks: List[str], n: int) -> int:
    """CPU runs one task per unit time; the same task needs n units of cooldown. Min total time (idle allowed).

    least_interval(["A","A","A","B","B","B"], 2) -> 8
    Target: O(T). Greedy: always run the task with the most remaining count.
    """
    h = [-c for c in Counter(tasks).values()]
    heapq.heapify(h)
    cooling, time = deque(), 0  # (remaining_negative_count, ready_time)
    while h or cooling:
        time += 1
        if h:
            c = 1 + heapq.heappop(h)  # one run used (counts are negative)
            if c:
                cooling.append((c, time + n))
        if cooling and cooling[0][1] == time:
            heapq.heappush(h, cooling.popleft()[0])
    return time


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted linked lists into one sorted list.

    Target: O(N log k). Heap holds the current head of each list.
    """
    h = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(h)  # index i breaks ties so nodes are never compared
    dummy = tail = ListNode()
    while h:
        _, i, node = heapq.heappop(h)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(h, (node.next.val, i, node.next))
    return dummy.next
