"""Section 07 - Linked Lists (reference solutions)."""
from typing import Optional

from helpers import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list; return the new head.

    1->2->3 becomes 3->2->1
    Target: O(n) time, O(1) space.
    """
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev, head = head, nxt
    return prev


def merge_two_lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted lists into one sorted list (reuse the nodes).

    1->2->4 + 1->3->4 -> 1->1->2->3->4->4
    Target: O(n + m).
    """
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


def has_cycle(head: Optional[ListNode]) -> bool:
    """True if the list has a cycle.

    Target: O(n) time, O(1) space (Floyd: slow/fast pointers).
    """
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove the n-th node from the END (1-indexed) and return the head.

    1->2->3->4->5, n=2 -> 1->2->3->5
    Target: one pass. Hint: dummy node + two pointers n apart.
    """
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return the middle node (second middle if even length).

    1->2->3->4->5 -> node 3 ; 1->2->3->4->5->6 -> node 4
    Target: one pass.
    """
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


def reorder_list(head: Optional[ListNode]) -> None:
    """Reorder IN PLACE: L0->L1->...->Ln becomes L0->Ln->L1->Ln-1->L2->...

    1->2->3->4 becomes 1->4->2->3
    Target: O(n) time, O(1) space. Combines middle + reverse + interleave.
    """
    if not head or not head.next:
        return
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
    second, slow.next = slow.next, None  # split into two halves
    prev = None
    while second:  # reverse second half
        nxt = second.next
        second.next = prev
        prev, second = second, nxt
    first, second = head, prev
    while second:  # interleave
        n1, n2 = first.next, second.next
        first.next, second.next = second, n1
        first, second = n1, n2


def add_two_numbers(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    """Digits are stored in REVERSE order (ones digit first). Return the sum as a list.

    2->4->3 (342) + 5->6->4 (465) = 7->0->8 (807)
    Target: O(max(n, m)).
    """
    dummy = tail = ListNode()
    carry = 0
    while a or b or carry:
        total = carry + (a.val if a else 0) + (b.val if b else 0)
        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next
        a = a.next if a else None
        b = b.next if b else None
    return dummy.next
