import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("s,exp", [("()", True), ("()[]{}", True), ("(]", False), ("([)]", False), ("{[]}", True), ("", True), ("((", False)])
def test_is_valid(s, exp):
    assert m.is_valid(s) is exp


@pytest.mark.parametrize("t,exp", [([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]), ([30, 40, 50, 60], [1, 1, 1, 0]), ([30, 20, 10], [0, 0, 0])])
def test_daily_temperatures(t, exp):
    assert m.daily_temperatures(t) == exp


@pytest.mark.parametrize("tokens,exp", [
    (["2", "1", "+", "3", "*"], 9), (["4", "13", "5", "/", "+"], 6), (["4", "-2", "/"], -2),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
])
def test_eval_rpn(tokens, exp):
    assert m.eval_rpn(tokens) == exp


@pytest.mark.parametrize("h,exp", [([2, 1, 5, 6, 2, 3], 10), ([2, 4], 4), ([1], 1), ([2, 1, 2], 3)])
def test_largest_rectangle_area(h, exp):
    assert m.largest_rectangle_area(list(h)) == exp


def test_min_stack():
    s = m.MinStack()
    s.push(-2); s.push(0); s.push(-3)
    assert s.get_min() == -3
    s.pop()
    assert s.top() == 0
    assert s.get_min() == -2
