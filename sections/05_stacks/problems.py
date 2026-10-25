'Section 05 - Stacks & Monotonic Stacks (your workspace).'


from typing import List


def is_valid(s: str) -> bool:
    """True if every bracket in s ()[]{} is closed in the correct order.

    is_valid("([{}])") -> True ; is_valid("(]") -> False
    Target: O(n).
    """
    pass


def daily_temperatures(temps: List[int]) -> List[int]:
    """For each day, how many days until a warmer temperature? (0 if never)

    daily_temperatures([73,74,75,71,69,72,76,73]) -> [1,1,4,2,1,1,0,0]
    Target: O(n) - monotonic (decreasing) stack of indices.
    """
    pass


def eval_rpn(tokens: List[str]) -> int:
    """Evaluate a Reverse Polish Notation expression. Division truncates toward zero.

    eval_rpn(["2","1","+","3","*"]) -> 9
    Target: O(n).
    """
    pass


def largest_rectangle_area(heights: List[int]) -> int:
    """Largest rectangle that fits inside a histogram.

    largest_rectangle_area([2,1,5,6,2,3]) -> 10
    Target: O(n) - monotonic increasing stack of (start_index, height).
    """
    pass


class MinStack:
    """Stack supporting push, pop, top and get_min - all in O(1)."""

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def get_min(self) -> int:
        pass
