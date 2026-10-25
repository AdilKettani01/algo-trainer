# 17 - Sorting & Selection

Python's built-in `sorted` / `list.sort` is **Timsort**: O(n log n), stable. In real code always use it; learn the algorithms to adapt their *ideas*.

| Algorithm | Best | Average | Worst | Space | Stable | Idea |
|---|---|---|---|---|---|---|
| Bubble / Insertion / Selection | n / n / n² | n² | n² | O(1) | B,I yes | simple; insertion great for tiny/nearly-sorted |
| **Merge sort** | n log n | n log n | n log n | O(n) | yes | divide, sort halves, merge |
| **Quick sort** | n log n | n log n | n² | O(log n) | no | partition around a pivot (randomise it!) |
| **Heap sort** | n log n | n log n | n log n | O(1) | no | build max-heap, repeatedly extract |
| Counting / Radix / Bucket | | n + k | | O(n + k) | yes | no comparisons; small integer ranges |

Comparison sorts can't beat **Ω(n log n)**.

## Merge sort
Split → recursively sort → **merge** two sorted halves with two pointers. Merging is where you can *count things*: **inversions** = every time a right element jumps ahead of the `len(left) - i` remaining left elements.

## Quicksort & quickselect
Partition into `< pivot`, `== pivot`, `> pivot` (3-way handles duplicates). Quicksort recurses into both sides; **quickselect** recurses into only the side containing the k-th element → **O(n) expected** (powers "k-th largest").

## Heap sort
Heapify in O(n) (sift down from `n//2-1` to 0), then swap root with the last element, shrink, sift down.

## Dutch national flag (3 values)
Three pointers `lo, i, hi`: 0 → swap to front, 2 → swap to back (don't advance `i` after a back-swap), 1 → move on. One pass, O(1) space.

## Sorting as a technique
Sorting first often unlocks greedy / two-pointer / binary search solutions (intervals, 3Sum, meeting rooms). Custom orders: `sorted(a, key=lambda x: (-x.score, x.name))`.

## Pitfalls
- Quicksort with first-element pivot degrades to O(n²) on sorted input → random pivot.
- `sort()` returns `None` (in place); `sorted()` returns a new list.

**Practice:** `merge_sort`, `quick_sort`, `heap_sort`, `quickselect`, `sort_colors`, `count_inversions`.
