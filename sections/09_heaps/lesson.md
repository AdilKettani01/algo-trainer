# 09 - Heaps / Priority Queues

A heap gives the smallest (or largest) item in **O(1)**, push/pop in **O(log n)**. Python's `heapq` is a **min-heap on a list**:
```python
import heapq
h = []; heapq.heappush(h, 5); heapq.heappop(h); h[0]   # peek min
heapq.heapify(lst)                                    # O(n)
heapq.nsmallest(k, items, key=...)  # / nlargest
```
**Max-heap trick:** store negatives. **Tuples** compare left to right: `(priority, tiebreak, payload)`.

## Patterns
1. **Top-K with a size-K heap**: for the K *largest*, keep a **min**-heap of size K - pop whenever it grows past K; the root is the K-th largest. O(n log k).
2. **Two heaps (running median)**: max-heap for the lower half, min-heap for the upper half, sizes differ by ≤ 1. Median is the top(s).
3. **Merge K sorted lists/streams**: heap of the current head of each; pop smallest, push its successor. O(N log k). Add an index tiebreaker so nodes are never compared.
4. **Greedy + heap** (task scheduler, last stone, meeting rooms): always process the most urgent / largest item; use a queue for cooldowns.
5. Dijkstra and Prim (section 11) are heap algorithms.

## Complexity cheat
- Build from n items: O(n) (`heapify`) vs O(n log n) by repeated push.
- Top-k via sort: O(n log n); via heap: O(n log k); via quickselect: O(n) average.

## Pitfalls
- No built-in max-heap or decrease-key. Use "lazy deletion": push a new entry, skip stale ones when popped.
- `heap[0]` is the min only; the rest of the list is *not* sorted.

**Practice:** `find_kth_largest`, `last_stone_weight`, `k_closest`, `MedianFinder`, `least_interval`, `merge_k_lists`.
