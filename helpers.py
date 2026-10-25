"""Shared data structures + the loader that tests use.

Tests load YOUR code (sections/<name>/problems.py) by default.
Set USE_SOLUTIONS=1 to run the same tests against solutions/<name>.py.
"""
import importlib.util
import os
import pathlib
from collections import deque

ROOT = pathlib.Path(__file__).parent


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(vals):
    dummy = tail = ListNode()
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(node, limit=10_000):
    out = []
    while node and len(out) < limit:
        out.append(node.val)
        node = node.next
    return out


def build_cycle(vals, pos):
    """Linked list whose tail points back to index `pos` (-1 = no cycle)."""
    head = build_list(vals)
    if pos >= 0 and head:
        nodes, cur = [], head
        while cur:
            nodes.append(cur)
            cur = cur.next
        nodes[-1].next = nodes[pos]
    return head


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    """LeetCode-style level order list, e.g. [3, 9, 20, None, None, 15, 7]."""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q, i = deque([root]), 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        n = q.popleft()
        if n is None:
            out.append(None)
            continue
        out.append(n.val)
        q.append(n.left)
        q.append(n.right)
    while out and out[-1] is None:
        out.pop()
    return out


def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def load(test_file):
    """Import problems.py (yours) or solutions/<section>.py for a test file."""
    section_dir = pathlib.Path(test_file).parent
    if os.environ.get("USE_SOLUTIONS") == "1":
        path = ROOT / "solutions" / f"{section_dir.name}.py"
    else:
        path = section_dir / "problems.py"
    spec = importlib.util.spec_from_file_location(f"mod_{section_dir.name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
