# 12 - Backtracking

## Idea
Build a solution step by step. At each step **choose → explore → un-choose**. If a partial solution can't work, abandon it (prune). It's DFS over a *decision tree*.

## Universal template
```python
def solve(...):
    res, path = [], []
    def go(state):
        if is_complete(state):
            res.append(path[:])         # COPY - path keeps mutating
            return
        for choice in choices(state):
            if not valid(choice): continue
            path.append(choice)         # choose
            go(next_state)              # explore
            path.pop()                  # un-choose
    go(initial)
    return res
```

## Recognising the shape
| Problem family | Decision at each step | Trick |
|---|---|---|
| Subsets | take / skip element `i` (or loop `start..n`) | record path at *every* node |
| Permutations | pick any unused element | `used[]` array |
| Combinations / combination sum | pick from index `start` onward | pass `i` (reuse) or `i+1` (no reuse) so you never generate reorderings |
| Duplicates in input | sort first | `if i > start and a[i] == a[i-1]: continue` |
| Parentheses | add `(` or `)` | only `(` if opened < n; only `)` if closed < opened |
| Grid word search | 4 directions | mark cell visited, **un-mark on return** |
| N-Queens | one queen per row | sets for columns & both diagonals (`r-c`, `r+c`) |

## Complexity
Often exponential: subsets O(n·2ⁿ), permutations O(n·n!). Pruning is what makes it practical.

## Pitfalls
- Forgetting `path[:]` (appending the same list object).
- Forgetting to undo state (visited marks, sets).
- Not pruning early (check `remaining < 0` before recursing).
- Memoise when subproblems repeat → that's dynamic programming (next sections).

**Practice:** `subsets`, `subsets_with_dup`, `permutations`, `combination_sum`, `generate_parenthesis`, `exist`, `total_n_queens`.
