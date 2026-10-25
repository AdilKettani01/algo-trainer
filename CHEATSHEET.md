# Cheat sheet

## 1. Constraints → target complexity
| n | Aim for | Typical technique |
|---|---|---|
| ≤ 10-12 | O(n!) | permutations, brute force |
| ≤ 20-25 | O(2ⁿ) | backtracking, bitmask |
| ≤ 500 | O(n³) | 3-nested DP, Floyd-Warshall |
| ≤ 5,000 | O(n²) | 2-D DP, nested loops |
| ≤ 10⁵ | O(n log n) | sort, heap, binary search, segment tree |
| ≤ 10⁶-10⁷ | O(n) | hashing, two pointers, sliding window, prefix sums |
| ≤ 10⁹+ | O(log n) / O(1) | binary search, math |

## 2. Problem wording → technique
| If the problem says... | Think |
|---|---|
| pair / triplet with a sum | hash map, or sort + two pointers |
| sorted array | binary search, two pointers |
| contiguous subarray / substring, longest/shortest | sliding window (positives) / prefix sums + map |
| count subarrays with sum k | prefix sum + hash map |
| next greater / smaller | monotonic stack |
| top k / k-th / streaming median | heap (or quickselect) |
| merge k sorted | heap |
| shortest path, unweighted | BFS |
| shortest path, weighted ≥ 0 | Dijkstra |
| ordering with dependencies / cycle in directed graph | topological sort |
| connected groups, "are these connected" | union-find / DFS |
| all combinations / permutations / subsets | backtracking |
| min / max / count ways, choices overlap | DP |
| intervals | sort, then greedy / sweep |
| "at most k", "minimum days/speed/capacity" | binary search on the answer |
| prefix of strings, autocomplete | trie |
| cache with eviction | hash map + linked list |
| single number among pairs, parity | XOR |
| tree problem | recursion returning a value, plus `nonlocal best` |

## 3. Python quick reference
```python
from collections import Counter, defaultdict, deque, OrderedDict
import heapq, bisect, itertools, functools, math

Counter("aab")                    # {'a': 2, 'b': 1}
defaultdict(list)                 # missing key -> []
deque([1,2]); dq.popleft()        # O(1) both ends
heapq.heappush(h, x); heappop(h)  # min-heap; negate for max-heap
bisect.bisect_left(a, x)          # lower bound
sorted(a, key=lambda x: (-x[1], x[0]))
@functools.lru_cache(None)        # memoise recursion
math.inf, float("-inf")
a[::-1]; a[l:r]; "".join(parts)   # slicing copies - O(k)
divmod(a, b); a // b; -(-a // b)  # floor div; ceil div
sys.setrecursionlimit(10**6)      # only if you must recurse deep
```
Gotchas: lists aren't hashable (use tuples) · `[[0]*m]*n` shares rows (use a comprehension) · `list.sort()` returns None · mutable default arguments · copy with `path[:]` before storing.

## 4. Complexity of common operations (Python)
| Op | Cost |
|---|---|
| list index / append / pop() | O(1) |
| list insert / pop(0) / `x in list` | O(n) |
| dict / set get, add, `in` | O(1) avg |
| `sorted`, `.sort()` | O(n log n) |
| slicing a[l:r] | O(r - l) |
| string concat in a loop | O(n²) → use join |
| heappush / heappop | O(log n) |
| deque append / popleft | O(1) |
