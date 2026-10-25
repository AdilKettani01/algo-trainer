import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("s,exp", [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True), ("0P", False)])
def test_is_palindrome(s, exp):
    assert m.is_palindrome(s) is exp


@pytest.mark.parametrize("nums,t,exp", [([2, 7, 11, 15], 9, [1, 2]), ([2, 3, 4], 6, [1, 3]), ([-1, 0], -1, [1, 2])])
def test_two_sum_sorted(nums, t, exp):
    assert m.two_sum_sorted(nums, t) == exp


@pytest.mark.parametrize("nums,exp", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]), ([0, 1, 1], []), ([0, 0, 0, 0], [[0, 0, 0]]),
])
def test_three_sum(nums, exp):
    res = m.three_sum(list(nums))
    assert sorted(sorted(t) for t in res) == exp


@pytest.mark.parametrize("h,exp", [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([4, 3, 2, 1, 4], 16)])
def test_max_area(h, exp):
    assert m.max_area(h) == exp


@pytest.mark.parametrize("h,exp", [([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6), ([4, 2, 0, 3, 2, 5], 9), ([], 0), ([3], 0)])
def test_trap(h, exp):
    assert m.trap(h) == exp


@pytest.mark.parametrize("nums,k", [([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5), ([1, 1, 2], 2), ([], 0), ([7], 1)])
def test_remove_duplicates(nums, k):
    nums = list(nums)
    expected = sorted(set(nums))
    assert m.remove_duplicates(nums) == k
    assert nums[:k] == expected
