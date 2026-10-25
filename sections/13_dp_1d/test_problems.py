import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("n,exp", [(1, 1), (2, 2), (3, 3), (10, 89), (45, 1836311903)])
def test_climb_stairs(n, exp):
    assert m.climb_stairs(n) == exp


@pytest.mark.parametrize("nums,exp", [([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12), ([5], 5), ([], 0)])
def test_rob(nums, exp):
    assert m.rob(nums) == exp


@pytest.mark.parametrize("nums,exp", [([2, 3, 2], 3), ([1, 2, 3, 1], 4), ([1], 1), ([1, 2, 3], 3)])
def test_rob_circular(nums, exp):
    assert m.rob_circular(nums) == exp


@pytest.mark.parametrize("coins,amt,exp", [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0), ([186, 419, 83, 408], 6249, 20)])
def test_coin_change(coins, amt, exp):
    assert m.coin_change(coins, amt) == exp


@pytest.mark.parametrize("nums,exp", [([10, 9, 2, 5, 3, 7, 101, 18], 4), ([0, 1, 0, 3, 2, 3], 4), ([7, 7, 7], 1), ([1], 1)])
def test_length_of_lis(nums, exp):
    assert m.length_of_lis(nums) == exp


@pytest.mark.parametrize("s,words,exp", [("leetcode", ["leet", "code"], True), ("applepenapple", ["apple", "pen"], True), ("catsandog", ["cats", "dog", "sand", "and", "cat"], False)])
def test_word_break(s, words, exp):
    assert m.word_break(s, words) is exp


@pytest.mark.parametrize("s,exp", [("12", 2), ("226", 3), ("06", 0), ("10", 1), ("2101", 1), ("0", 0)])
def test_num_decodings(s, exp):
    assert m.num_decodings(s) == exp


@pytest.mark.parametrize("nums,exp", [([2, 3, -2, 4], 6), ([-2, 0, -1], 0), ([-2, 3, -4], 24), ([-3], -3)])
def test_max_product_subarray(nums, exp):
    assert m.max_product_subarray(nums) == exp
