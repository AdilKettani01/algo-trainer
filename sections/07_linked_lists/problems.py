'Section 07 - Linked Lists (your workspace).'


from typing import Optional


from helpers import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list; return the new head.

    1->2->3 becomes 3->2->1
    Target: O(n) time, O(1) space.
    """
    pass


def merge_two_lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted lists into one sorted list (reuse the nodes).

    1->2->4 + 1->3->4 -> 1->1->2->3->4->4
    Target: O(n + m).
    """
    pass


def has_cycle(head: Optional[ListNode]) -> bool:
    """True if the list has a cycle.

    Target: O(n) time, O(1) space (Floyd: slow/fast pointers).
    """
    pass


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove the n-th node from the END (1-indexed) and return the head.

    1->2->3->4->5, n=2 -> 1->2->3->5
    Target: one pass. Hint: dummy node + two pointers n apart.
    """
    pass


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return the middle node (second middle if even length).

    1->2->3->4->5 -> node 3 ; 1->2->3->4->5->6 -> node 4
    Target: one pass.
    """
    pass


def reorder_list(head: Optional[ListNode]) -> None:
    """Reorder IN PLACE: L0->L1->...->Ln becomes L0->Ln->L1->Ln-1->L2->...

    1->2->3->4 becomes 1->4->2->3
    Target: O(n) time, O(1) space. Combines middle + reverse + interleave.
    """
    pass


def add_two_numbers(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    """Digits are stored in REVERSE order (ones digit first). Return the sum as a list.

    2->4->3 (342) + 5->6->4 (465) = 7->0->8 (807)
    Target: O(max(n, m)).
    """
    pass
