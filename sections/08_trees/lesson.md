# 08 - Binary Trees & BSTs

`TreeNode(val, left, right)`. Tests build trees from LeetCode-style lists: `build_tree([3,9,20,None,None,15,7])`.

## The recursion mindset
Solve for a node by trusting the answer for its children:
```python
def depth(node):
    if not node: return 0
    return 1 + max(depth(node.left), depth(node.right))
```
Define: **what does my function return?** and **what extra info do I need to carry** (bounds, running sum)?

## Traversals
- **DFS**: pre-order (node, L, R), in-order (L, node, R - *sorted order for a BST*), post-order (L, R, node - children first).
- **BFS / level order**: queue; process `len(queue)` nodes per level.

## Patterns
1. **Return a value up** (depth, diameter, max path sum): compute height from children, update a *global/nonlocal best* using both children, return the one-sided value. Diameter = max(`h(left) + h(right)`). Max path sum ignores negative branches (`max(gain, 0)`).
2. **Pass info down** (valid BST): carry `(low, high)` bounds - checking only parent vs child is *wrong* (the 5/4/6/3/7 trap).
3. **Lowest common ancestor**: if both sides return non-null, the current node is the LCA; else return the non-null side.
4. **BST properties**: left < node < right → search/insert in O(h); in-order = sorted → k-th smallest with iterative in-order.

## Complexity
Time O(n); space O(h) recursion (h = log n balanced, n worst case). For deep trees use an explicit stack to avoid Python's recursion limit.

## Pitfalls
- Empty tree (`None`) is a valid input - handle it first.
- Mutating vs returning: `invert_tree` returns the root.

**Practice:** `max_depth`, `invert_tree`, `level_order`, `is_valid_bst`, `lowest_common_ancestor`, `diameter_of_binary_tree`, `kth_smallest`, `max_path_sum`.
