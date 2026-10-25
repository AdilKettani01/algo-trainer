# 04 - Prefix Sums & Intervals

## Prefix sums
`prefix[i] = a[0] + ... + a[i-1]`, so **sum(a[l..r]) = prefix[r+1] - prefix[l]** in O(1) after O(n) setup.

### Prefix sum + hash map
"Count/find subarrays with sum = k" (works with negatives, unlike sliding window):
```python
seen = {0: 1}; running = 0; count = 0
for x in a:
    running += x
    count += seen.get(running - k, 0)   # earlier prefix that leaves exactly k
    seen[running] = seen.get(running, 0) + 1
```
Variants: store the *first index* of each prefix for "longest subarray" (e.g. equal 0s and 1s → map 0→-1, then longest sum-0).
Same idea in 2D (prefix over rows & columns), and as a **difference array** for many range-add updates.

## Intervals
Almost every interval problem starts with **sorting**.
1. **Merge**: sort by start; if `start <= last_end` extend `last_end`, else begin a new interval.
2. **Overlap count / rooms (sweep line)**: sort starts and ends separately; walk starts - if the earliest unfinished end is ≤ start, reuse a room, else add one.
3. **Insert interval**: three phases - before / overlapping / after.
4. Greedy interval scheduling (section 15) sorts by **end** time instead.

## Pitfalls
- Decide whether touching intervals (`[1,2]`,`[2,3]`) overlap - it changes `<` vs `<=`.
- Don't mutate the caller's lists unless allowed.

**Practice:** `NumArray`, `subarray_sum`, `find_max_length`, `merge`, `min_meeting_rooms`.
