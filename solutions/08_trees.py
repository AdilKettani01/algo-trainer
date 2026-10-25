"""Section 08 - Binary Trees & BSTs (reference solutions)."""
from collections import deque
from typing import List, Optional

from helpers import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    """Number of nodes on the longest root-to-leaf path (empty tree -> 0).

    Target: O(n). Hint: recursion - 1 + max(left, right).
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Mirror the tree (swap left and right everywhere) and return the root.

    Target: O(n).
    """
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Values level by level, left to right.

    [3,9,20,None,None,15,7] -> [[3],[9,20],[15,7]]
    Target: O(n) with BFS (queue).
    """
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):  # exactly one level per outer loop
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """True if the tree is a valid binary SEARCH tree (strict: left < node < right, for ALL descendants).

    Target: O(n). Hint: pass down (low, high) bounds.
    """
    def go(node, lo, hi):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return go(node.left, lo, node.val) and go(node.right, node.val, hi)

    return go(root, float("-inf"), float("inf"))


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """Lowest common ancestor of nodes p and q in a general binary tree (a node can be its own ancestor).

    Target: O(n).
    """
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if left and right else left or right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """Length (in EDGES) of the longest path between any two nodes.

    [1,2,3,4,5] -> 3
    Target: O(n). Hint: at each node, best path through it = height(left) + height(right).
    """
    best = 0

    def height(node):
        nonlocal best
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)

    height(root)
    return best


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """k-th smallest value (1-indexed) in a BST.

    Target: O(h + k). Hint: in-order traversal visits a BST in sorted order.
    """
    stack, node = [], root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right


def max_path_sum(root: Optional[TreeNode]) -> int:
    """Maximum sum over any path (any start, any end, at least one node). Values may be negative.

    [-10,9,20,None,None,15,7] -> 42
    Target: O(n).
    """
    best = float("-inf")

    def gain(node):
        nonlocal best
        if not node:
            return 0
        l, r = max(gain(node.left), 0), max(gain(node.right), 0)  # ignore negative branches
        best = max(best, node.val + l + r)
        return node.val + max(l, r)

    gain(root)
    return best
