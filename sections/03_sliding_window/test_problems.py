import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("nums,k,exp", [([2, 1, 5, 1, 3, 2], 3, 9), ([2, 3, 4, 1, 5], 2, 7), ([5], 1, 5)])
def test_max_sum_subarray(nums, k, exp):
    assert m.max_sum_subarray(nums, k) == exp


@pytest.mark.parametrize("s,exp", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0), ("abba", 2)])
def test_length_of_longest_substring(s, exp):
    assert m.length_of_longest_substring(s) == exp


@pytest.mark.parametrize("t,nums,exp", [(7, [2, 3, 1, 2, 4, 3], 2), (4, [1, 4, 4], 1), (11, [1] * 8, 0)])
def test_min_subarray_len(t, nums, exp):
    assert m.min_subarray_len(t, nums) == exp


@pytest.mark.parametrize("s,k,exp", [("ABAB", 2, 4), ("AABABBA", 1, 4), ("AAAA", 0, 4)])
def test_character_replacement(s, k, exp):
    assert m.character_replacement(s, k) == exp


@pytest.mark.parametrize("s,t,exp", [("ADOBECODEBANC", "ABC", "BANC"), ("a", "a", "a"), ("a", "aa", ""), ("ab", "b", "b")])
def test_min_window(s, t, exp):
    assert m.min_window(s, t) == exp
