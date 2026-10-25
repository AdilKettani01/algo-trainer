# 05 - Stacks & Monotonic Stacks

## Stack = LIFO
Python `list`: `append` / `pop` are O(1). Use a stack when the *most recent unfinished thing* matters: matching brackets, undo, expression evaluation, DFS.

## Matching pairs
Push openers; on a closer, pop and compare. Empty stack at the end ⇒ balanced.

## Expression evaluation (RPN)
Numbers push; an operator pops `b` then `a`, pushes `a op b`. Watch operand order for `-` and `/`; truncate division toward zero with `int(a / b)` (not `//`).

## Monotonic stack - "next greater / smaller element"
Keep a stack whose values are always sorted (e.g. decreasing). When a new value breaks the order, pop and *resolve* every popped element - the new value is their answer.
```python
st = []                       # indices with decreasing temps
for i, t in enumerate(temps):
    while st and temps[st[-1]] < t:
        j = st.pop(); ans[j] = i - j
    st.append(i)
```
Each element is pushed and popped once → **O(n)**.

**Largest rectangle in histogram**: keep an *increasing* stack of `(start, height)`. A shorter bar pops taller ones; each popped bar's rectangle spans from its `start` to the current index. A sentinel `0` at the end flushes everything.

## Min stack
Store `(value, min_so_far)` per entry so `get_min` is O(1).

## Pitfalls
- Store **indices** (not values) when you need distances.
- Decide strict vs non-strict comparison for equal values.

**Practice:** `is_valid`, `daily_temperatures`, `eval_rpn`, `largest_rectangle_area`, `MinStack`.
