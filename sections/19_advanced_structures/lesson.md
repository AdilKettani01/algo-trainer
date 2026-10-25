# 19 - Advanced Data Structures

## LRU Cache
Need O(1) `get` and `put` with eviction of the **least recently used** key.
- Hash map `key → node` + **doubly linked list** ordered by recency (head = most recent). On access: unlink + move to head. On overflow: remove the tail.
- In Python, `OrderedDict` is exactly that: `move_to_end(key)` and `popitem(last=False)`.
Related: LFU cache, TTL cache, `functools.lru_cache`.

## Fenwick Tree (Binary Indexed Tree)
Point update + prefix sum, both O(log n), in an array the size of the input.
- `i & -i` isolates the lowest set bit: it's the size of the range node `i` covers.
- `update`: `i += i & -i` (go to parents). `query`: `i -= i & -i` (strip bits).
- Range sum = `prefix(r) - prefix(l-1)`. Use for counting inversions, order statistics, dynamic prefix sums.

## Segment Tree
Stores an aggregate (sum / min / max / gcd) for ranges. Point update + range query in O(log n). Bottom-up array version: leaves at `t[n:]`, parent of `i` is `i // 2`, node `i` = combine(`2i`, `2i+1`). Supports any **associative** operation; **lazy propagation** extends it to range updates.

Fenwick vs segment tree: Fenwick is shorter/faster but limited to invertible ops (sum, xor); segment trees handle min/max and range updates.

## Monotonic deque
Sliding-window maximum in O(n): keep a deque of indices whose values are **decreasing**. Pop from the back while the new value is ≥ them (they can never be a window max again); pop from the front when the index leaves the window. The front is the max.

## Other structures worth knowing
| Structure | Gives you |
|---|---|
| Union-Find | dynamic connectivity (section 11) |
| Sparse table | O(1) range-min on static arrays, O(n log n) build |
| Balanced BST / `SortedList` (`sortedcontainers`) | ordered sets, floor/ceiling, rank |
| Bloom filter | probabilistic membership |
| Skip list | simple ordered map |
| Interval tree | overlap queries |
| Deque / monotonic queue | window extrema |

## Choosing a structure (ask)
1. What operations, and how often (reads vs writes)?
2. Do I need order? min/max? ranges? recency?
3. Static data (preprocess once) or dynamic (updates)?

**Practice:** `LRUCache`, `FenwickTree`, `SegmentTree`, `sliding_window_maximum`.
