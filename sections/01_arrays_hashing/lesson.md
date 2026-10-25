# 01 - Complexity, Arrays & Hashing

## Big-O in one minute
Big-O counts how work grows with input size `n`, ignoring constants.

| Class        | Name                    | Typical example          |
|--------------|-------------------------|--------------------------|
| O(1)         | constant                | dict lookup, array index |
| O(log n)     | logarithmic             | binary search            |
| O(n)         | linear                  | one loop                 |
| O(n log n)   | linearithmic            | sorting                  |
| O(n²)        | quadratic               | nested loops             |
| O(2ⁿ), O(n!) | exponential / factorial | subsets, permutations    |

Rule of thumb for tests (≈10⁸ simple ops/sec in a fast language, far less in Python):
`n ≤ 20` → exponential OK · `n ≤ 5,000` → O(n²) · `n ≤ 10⁵` → O(n log n) · `n ≤ 10⁶+` → O(n).
Space complexity counts extra memory you allocate (not the input).

## The hash map trade: memory for time
A `dict`/`set` gives average O(1) insert/lookup. Whenever you catch yourself writing a loop *inside* a loop just to "find something", ask: **can I store what I've seen in a dict and look it up instead?**

## Patterns
1. **Complement lookup** (Two Sum): for each `x`, check whether `target - x` was already seen.
2. **Frequency counting**: `Counter(items)` → anagrams, top-k, majority.
3. **Canonical key**: map different-looking things to one key (`tuple(sorted(word))` groups anagrams).
4. **Set for existence / dedupe**: `len(set(a)) < len(a)` ⇒ duplicate. Longest consecutive run: only start counting from numbers whose predecessor isn't in the set.
5. **Prefix / suffix products** (product except self): out[i] = (everything left) × (everything right), built in two passes.

## Template
```python
seen = {}
for i, x in enumerate(nums):
    if need(x) in seen:
        return answer(seen[need(x)], i)
    seen[x] = i
```

## Pitfalls
- Check *before* inserting so an element doesn't match itself.
- Lists aren't hashable → use `tuple(...)` for dict keys.
- `Counter` comparison is O(n) but `sorted()` comparison is O(n log n).

**Practice:** `two_sum`, `contains_duplicate`, `is_anagram`, `group_anagrams`, `top_k_frequent`, `product_except_self`, `longest_consecutive`.
