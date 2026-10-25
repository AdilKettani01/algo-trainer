# 02 - Two Pointers

## When to use
Sorted array / string, or a problem about pairs, palindromes, partitioning or "squeezing" a range. Replaces an O(n²) pair search with O(n).

## Variants
1. **Opposite ends (converging)**: `l = 0`, `r = n-1`, move inward based on a comparison.
   - Sorted two-sum: sum too small → `l += 1`; too big → `r -= 1`.
   - Container with most water: always move the *shorter* wall (the taller one can never help while the short one limits you).
   - Trapping rain water: move the side with the smaller max; its water level is already decided by that max.
2. **Fixed anchor + inner pair** (3Sum): sort, fix `a`, run converging pointers on the rest. Skip duplicates at every level to avoid repeated triplets.
3. **Slow / fast (same direction)**: `slow` writes, `fast` reads. In-place dedupe, remove element, move zeroes.

## Template (converging)
```python
l, r = 0, len(a) - 1
while l < r:
    s = a[l] + a[r]
    if s == target: ...
    elif s < target: l += 1
    else: r -= 1
```

## Why it is correct
Each step *eliminates* candidates for good. In sorted two-sum, if `a[l] + a[r]` is too small, `a[l]` can't pair with anything ≤ `a[r]`, so discarding `l` loses nothing.

## Pitfalls
- Sorting changes indices - if you must return original indices, store `(value, index)` first.
- Duplicate skipping in 3Sum: skip *after* recording a hit, and skip repeated anchors.
- Use `while l < r` (not `<=`) when a pair needs two different elements.

**Practice:** `is_palindrome`, `two_sum_sorted`, `three_sum`, `max_area`, `trap`, `remove_duplicates`.
