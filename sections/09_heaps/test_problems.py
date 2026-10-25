import pytest
from helpers import load, build_list, to_list

m = load(__file__)


@pytest.mark.parametrize("nums,k,exp", [([3, 2, 1, 5, 6, 4], 2, 5), ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4), ([1], 1, 1)])
def test_find_kth_largest(nums, k, exp):
    assert m.find_kth_largest(nums, k) == exp


@pytest.mark.parametrize("s,exp", [([2, 7, 4, 1, 8, 1], 1), ([1], 1), ([2, 2], 0)])
def test_last_stone_weight(s, exp):
    assert m.last_stone_weight(s) == exp


@pytest.mark.parametrize("pts,k,exp", [([[1, 3], [-2, 2]], 1, [[-2, 2]]), ([[3, 3], [5, -1], [-2, 4]], 2, [[-2, 4], [3, 3]])])
def test_k_closest(pts, k, exp):
    assert sorted(m.k_closest(pts, k)) == sorted(exp)


def test_median_finder():
    mf = m.MedianFinder()
    mf.add_num(1); mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2
    for x in (10, -5, 7):
        mf.add_num(x)
    assert mf.find_median() == 2.5  # sorted: -5 1 2 3 7 10


@pytest.mark.parametrize("tasks,n,exp", [
    (list("AAABBB"), 2, 8), (list("AAABBB"), 0, 6), (list("AAAAAABCDEFG"), 2, 16),
])
def test_least_interval(tasks, n, exp):
    assert m.least_interval(tasks, n) == exp


@pytest.mark.parametrize("lists,exp", [([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]), ([], []), ([[]], []), ([[], [1]], [1])])
def test_merge_k_lists(lists, exp):
    assert to_list(m.merge_k_lists([build_list(x) for x in lists])) == exp
