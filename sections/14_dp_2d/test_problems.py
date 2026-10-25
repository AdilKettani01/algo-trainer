import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("r,c,exp", [(3, 7, 28), (3, 2, 3), (1, 1, 1), (10, 10, 48620)])
def test_unique_paths(r, c, exp):
    assert m.unique_paths(r, c) == exp


@pytest.mark.parametrize("g,exp", [([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7), ([[1, 2, 3], [4, 5, 6]], 12), ([[5]], 5)])
def test_min_path_sum(g, exp):
    assert m.min_path_sum(g) == exp


@pytest.mark.parametrize("a,b,exp", [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0), ("", "a", 0)])
def test_lcs(a, b, exp):
    assert m.longest_common_subsequence(a, b) == exp


@pytest.mark.parametrize("a,b,exp", [("horse", "ros", 3), ("intention", "execution", 5), ("", "a", 1), ("a", "", 1), ("abc", "abc", 0)])
def test_min_distance(a, b, exp):
    assert m.min_distance(a, b) == exp


@pytest.mark.parametrize("nums,exp", [([1, 5, 11, 5], True), ([1, 2, 3, 5], False), ([2, 2, 1, 1], True)])
def test_can_partition(nums, exp):
    assert m.can_partition(nums) is exp


@pytest.mark.parametrize("amt,coins,exp", [(5, [1, 2, 5], 4), (3, [2], 0), (10, [10], 1), (0, [7], 1)])
def test_coin_change_ways(amt, coins, exp):
    assert m.coin_change_ways(amt, coins) == exp


@pytest.mark.parametrize("w,v,cap,exp", [([1, 3, 4, 5], [1, 4, 5, 7], 7, 9), ([10], [5], 5, 0), ([2, 3, 4], [3, 4, 5], 5, 7)])
def test_knapsack_01(w, v, cap, exp):
    assert m.knapsack_01(w, v, cap) == exp


@pytest.mark.parametrize("p,exp", [([1, 2, 3, 0, 2], 3), ([1], 0), ([1, 2, 4], 3)])
def test_max_profit_cooldown(p, exp):
    assert m.max_profit_cooldown(p) == exp
