# 07 - Linked Lists

`ListNode(val, next)`. No random access - you walk with pointers. Most solutions are O(n) time, O(1) space.

## Toolbox
1. **Dummy head**: `dummy = ListNode(0, head)` removes special cases when the head may change (remove, merge, insert).
2. **Reverse in place**:
```python
prev = None
while head:
    nxt = head.next      # save
    head.next = prev     # flip
    prev, head = head, nxt
return prev
```
3. **Slow / fast pointers** (Floyd):
   - middle: `fast` moves 2, `slow` moves 1 → slow is at the middle.
   - cycle: if they ever meet, there's a cycle.
4. **Gap pointers**: advance `fast` n steps first, then move both → `slow` ends n from the end (remove n-th from end).
5. **Merge two sorted lists**: dummy + tail, always attach the smaller head.
6. **Combine tools**: reorder list = find middle → reverse second half → interleave.
7. **Carry arithmetic**: add numbers digit by digit with a `carry`, loop while `a or b or carry`.

## Pitfalls
- Always draw boxes and arrows. Update pointers in the right order (save `next` first!).
- Cut the list (`slow.next = None`) when splitting, or you'll create a cycle.
- Guard against `None` before `.next.next`.
- Tests use `build_list([1,2,3])` and `to_list(head)` from `helpers.py`.

**Practice:** `reverse_list`, `merge_two_lists`, `has_cycle`, `remove_nth_from_end`, `middle_node`, `reorder_list`, `add_two_numbers`.
