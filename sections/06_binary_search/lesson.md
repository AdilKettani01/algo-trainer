# 06 - Binary Search

## When to use
Sorted data - **or any monotonic yes/no condition** ("is `x` big enough?" flips from False to True exactly once). Halves the search space: O(log n).

## Template A: find exact value
```python
lo, hi = 0, len(a) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if a[mid] == t: return mid
    if a[mid] < t: lo = mid + 1
    else: hi = mid - 1
return -1
```

## Template B: first index where condition is True (lower bound)
```python
lo, hi = 0, len(a)            # hi exclusive: answer may be len(a)
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid      # mid might be the answer - keep it
    else:       lo = mid + 1
return lo
```
Template B handles insert position, rotated-array minimum, and "binary search on the answer".

## Binary search on the answer
Don't search the array - search the **value**. Koko's bananas: `speed` too slow → can't finish in `h` hours; the feasibility check is monotonic. Write `feasible(x)` (O(n)), binary search `x` over `[lo, hi]` → O(n log range). Same pattern: ship packages in D days, split array largest sum, integer sqrt.

## Rotated sorted array
At any `mid`, **one half is sorted**. Decide which half contains the target by checking the sorted half's endpoints. For the minimum: compare `a[mid]` with `a[hi]`.

## Pitfalls
- Infinite loops: with `lo = mid` use the **upper** mid `(lo + hi + 1) // 2`.
- `(lo + hi) // 2` can overflow in C/Java (`lo + (hi-lo)//2`) - harmless in Python.
- Python has `bisect_left` / `bisect_right` - great in practice, but implement by hand for tests.

**Practice:** `search`, `search_insert`, `search_rotated`, `find_min`, `min_eating_speed`, `my_sqrt`.
