# 03 - Sliding Window

## When to use
"Longest / shortest / best **contiguous** subarray or substring such that ..." - and a condition you can maintain incrementally.

## Fixed-size window
Add the new right element, drop the one that left. O(n).
```python
window = sum(a[:k]); best = window
for i in range(k, len(a)):
    window += a[i] - a[i-k]
    best = max(best, window)
```

## Variable-size window (expand right, shrink left)
```python
l = 0
for r, x in enumerate(a):
    add(x)                      # expand
    while window_is_invalid():  # shrink until valid again
        remove(a[l]); l += 1
    best = max(best, r - l + 1)
```
- **Longest valid** window: shrink only while *invalid*; record after.
- **Shortest valid** window (min subarray len, min window substring): record while *valid*, shrink as far as you can.

## Key ideas per problem
- *Longest substring w/o repeats*: remember last index of each char; jump `l` past the previous copy.
- *Character replacement*: window is valid if `size - max_freq <= k`. You never need to shrink `max_freq` - a stale high value can't produce a wrong *larger* answer.
- *Minimum window substring*: keep a `need` counter and a `missing` count; when `missing == 0`, shrink.

## Complexity
Each pointer moves forward only → **O(n)** total even with the inner `while`.

## Pitfalls
- Works for **positive** numbers (min subarray len). With negatives, shrinking no longer monotonic → use prefix sums + hash map (section 04).
- Off-by-one: window length is `r - l + 1`.

**Practice:** `max_sum_subarray`, `length_of_longest_substring`, `min_subarray_len`, `character_replacement`, `min_window`.
