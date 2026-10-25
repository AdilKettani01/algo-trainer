'Section 08 - Binary Trees & BSTs (your workspace).'


from typing import List, Optional


from helpers import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    """Number of nodes on the longest root-to-leaf path (empty tree -> 0).

    Target: O(n). Hint: recursion - 1 + max(left, right).
    """
    pass


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Mirror the tree (swap left and right everywhere) and return the root.

    Target: O(n).
    """
    pass


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Values level by level, left to right.

    [3,9,20,None,None,15,7] -> [[3],[9,20],[15,7]]
    Target: O(n) with BFS (queue).
    """
    pass


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """True if the tree is a valid binary SEARCH tree (strict: left < node < right, for ALL descendants).

    Target: O(n). Hint: pass down (low, high) bounds.
    """
    pass


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """Lowest common ancestor of nodes p and q in a general binary tree (a node can be its own ancestor).

    Target: O(n).
    """
    pass


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """Length (in EDGES) of the longest path between any two nodes.

    [1,2,3,4,5] -> 3
    Target: O(n). Hint: at each node, best path through it = height(left) + height(right).
    """
    pass


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """k-th smallest value (1-indexed) in a BST.

    Target: O(h + k). Hint: in-order traversal visits a BST in sorted order.
    """
    pass


def max_path_sum(root: Optional[TreeNode]) -> int:
    """Maximum sum over any path (any start, any end, at least one node). Values may be negative.

    [-10,9,20,None,None,15,7] -> 42
    Target: O(n).
    """
    pass
