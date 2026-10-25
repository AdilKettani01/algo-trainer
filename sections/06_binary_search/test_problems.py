import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("nums,t,exp", [([-1, 0, 3, 5, 9, 12], 9, 4), ([-1, 0, 3, 5, 9, 12], 2, -1), ([5], 5, 0), ([], 1, -1)])
def test_search(nums, t, exp):
    assert m.search(nums, t) == exp


@pytest.mark.parametrize("nums,t,exp", [([1, 3, 5, 6], 5, 2), ([1, 3, 5, 6], 2, 1), ([1, 3, 5, 6], 7, 4), ([1, 3, 5, 6], 0, 0)])
def test_search_insert(nums, t, exp):
    assert m.search_insert(nums, t) == exp


@pytest.mark.parametrize("nums,t,exp", [([4, 5, 6, 7, 0, 1, 2], 0, 4), ([4, 5, 6, 7, 0, 1, 2], 3, -1), ([1], 0, -1), ([3, 1], 1, 1), ([5, 1, 3], 5, 0)])
def test_search_rotated(nums, t, exp):
    assert m.search_rotated(nums, t) == exp


@pytest.mark.parametrize("nums,exp", [([3, 4, 5, 1, 2], 1), ([4, 5, 6, 7, 0, 1, 2], 0), ([11, 13, 15, 17], 11), ([2, 1], 1)])
def test_find_min(nums, exp):
    assert m.find_min(nums) == exp


@pytest.mark.parametrize("piles,h,exp", [([3, 6, 7, 11], 8, 4), ([30, 11, 23, 4, 20], 5, 30), ([30, 11, 23, 4, 20], 6, 23)])
def test_min_eating_speed(piles, h, exp):
    assert m.min_eating_speed(piles, h) == exp


@pytest.mark.parametrize("x,exp", [(0, 0), (1, 1), (4, 2), (8, 2), (2147395599, 46339)])
def test_my_sqrt(x, exp):
    assert m.my_sqrt(x) == exp
