"""Section 05 - Stacks & Monotonic Stacks (reference solutions)."""
from typing import List


def is_valid(s: str) -> bool:
    """True if every bracket in s ()[]{} is closed in the correct order.

    is_valid("([{}])") -> True ; is_valid("(]") -> False
    Target: O(n).
    """
    pairs, st = {")": "(", "]": "[", "}": "{"}, []
    for ch in s:
        if ch in pairs:
            if not st or st.pop() != pairs[ch]:
                return False
        else:
            st.append(ch)
    return not st


def daily_temperatures(temps: List[int]) -> List[int]:
    """For each day, how many days until a warmer temperature? (0 if never)

    daily_temperatures([73,74,75,71,69,72,76,73]) -> [1,1,4,2,1,1,0,0]
    Target: O(n) - monotonic (decreasing) stack of indices.
    """
    res, st = [0] * len(temps), []
    for i, t in enumerate(temps):
        while st and temps[st[-1]] < t:  # today is warmer than those waiting
            j = st.pop()
            res[j] = i - j
        st.append(i)
    return res


def eval_rpn(tokens: List[str]) -> int:
    """Evaluate a Reverse Polish Notation expression. Division truncates toward zero.

    eval_rpn(["2","1","+","3","*"]) -> 9
    Target: O(n).
    """
    st = []
    for t in tokens:
        if t in {"+", "-", "*", "/"}:
            b, a = st.pop(), st.pop()
            if t == "+":
                st.append(a + b)
            elif t == "-":
                st.append(a - b)
            elif t == "*":
                st.append(a * b)
            else:
                st.append(int(a / b))
        else:
            st.append(int(t))
    return st[0]


def largest_rectangle_area(heights: List[int]) -> int:
    """Largest rectangle that fits inside a histogram.

    largest_rectangle_area([2,1,5,6,2,3]) -> 10
    Target: O(n) - monotonic increasing stack of (start_index, height).
    """
    st, best = [], 0
    for i, h in enumerate(heights + [0]):  # sentinel 0 flushes the stack
        start = i
        while st and st[-1][1] > h:
            idx, height = st.pop()
            best = max(best, height * (i - idx))
            start = idx  # new bar can extend left to where the taller bar began
        st.append((start, h))
    return best


class MinStack:
    """Stack supporting push, pop, top and get_min - all in O(1)."""

    def __init__(self):
        self.st = []  # (value, min_so_far)

    def push(self, val: int) -> None:
        cur_min = min(val, self.st[-1][1]) if self.st else val
        self.st.append((val, cur_min))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def get_min(self) -> int:
        return self.st[-1][1]
