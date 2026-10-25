# 15 - Greedy Algorithms

## Idea
Make the locally best choice at every step and never reconsider. It's fast (often O(n) or O(n log n)) but only valid when a **greedy-choice property** holds. If you can't argue why local ⇒ global, test against brute force or fall back to DP.

## How to justify (exchange argument)
"Suppose an optimal solution doesn't make my greedy choice. Swapping in my choice doesn't make it worse." Example: for non-overlapping intervals, picking the interval that **ends earliest** leaves the most room for the rest.

## Patterns
| Problem | Greedy rule |
|---|---|
| Kadane (max subarray) | drop a prefix whose running sum is negative: `cur = max(x, cur + x)` |
| Jump game | track `farthest` reachable; if `i > farthest` you're stuck |
| Jump game II | BFS-in-disguise: when you reach `cur_end`, take a jump to `farthest` |
| Gas station | if total gas < total cost → -1; else when the tank goes negative, the start must be after that point |
| Partition labels | extend the current part to the last occurrence of every letter inside it |
| Non-overlapping intervals | sort by **end**; keep an interval if it starts ≥ last kept end |
| Candy | two passes (left→right, right→left), take the max |

Also: Huffman coding (heap), fractional knapsack (sort by value/weight), activity selection, task scheduling by deadline.

## Greedy vs DP
- 0/1 knapsack, coin change with arbitrary coins → **not** greedy (use DP). Greedy works for canonical coin systems like US coins.
- If a choice can be *wrong* depending on later items, it's DP.

## Pitfalls
- Sorting key matters (start vs end; value/weight ratio).
- Greedy can *look* right on samples. Write a brute-force checker for small random inputs.

**Practice:** `max_sub_array`, `can_jump`, `jump`, `can_complete_circuit`, `partition_labels`, `erase_overlap_intervals`, `candy`.
