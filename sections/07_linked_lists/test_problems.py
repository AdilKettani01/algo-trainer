import pytest
from helpers import load, build_list, to_list, build_cycle

m = load(__file__)


@pytest.mark.parametrize("vals", [[1, 2, 3, 4, 5], [1, 2], [], [7]])
def test_reverse_list(vals):
    assert to_list(m.reverse_list(build_list(vals))) == vals[::-1]


@pytest.mark.parametrize("a,b,exp", [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]), ([], [], []), ([], [0], [0]), ([5], [1, 2], [1, 2, 5])])
def test_merge_two_lists(a, b, exp):
    assert to_list(m.merge_two_lists(build_list(a), build_list(b))) == exp


@pytest.mark.parametrize("vals,pos,exp", [([3, 2, 0, -4], 1, True), ([1, 2], 0, True), ([1], -1, False), ([1, 2, 3], -1, False), ([], -1, False)])
def test_has_cycle(vals, pos, exp):
    assert m.has_cycle(build_cycle(vals, pos)) is exp


@pytest.mark.parametrize("vals,n,exp", [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]), ([1], 1, []), ([1, 2], 1, [1]), ([1, 2], 2, [2])])
def test_remove_nth_from_end(vals, n, exp):
    assert to_list(m.remove_nth_from_end(build_list(vals), n)) == exp


@pytest.mark.parametrize("vals,exp", [([1, 2, 3, 4, 5], [3, 4, 5]), ([1, 2, 3, 4, 5, 6], [4, 5, 6]), ([1], [1])])
def test_middle_node(vals, exp):
    assert to_list(m.middle_node(build_list(vals))) == exp


@pytest.mark.parametrize("vals,exp", [([1, 2, 3, 4], [1, 4, 2, 3]), ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]), ([1], [1]), ([1, 2], [1, 2])])
def test_reorder_list(vals, exp):
    head = build_list(vals)
    m.reorder_list(head)
    assert to_list(head) == exp


@pytest.mark.parametrize("a,b,exp", [([2, 4, 3], [5, 6, 4], [7, 0, 8]), ([0], [0], [0]), ([9] * 7, [9] * 4, [8, 9, 9, 9, 0, 0, 0, 1])])
def test_add_two_numbers(a, b, exp):
    assert to_list(m.add_two_numbers(build_list(a), build_list(b))) == exp
