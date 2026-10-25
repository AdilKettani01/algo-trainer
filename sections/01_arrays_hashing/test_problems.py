import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("nums,target", [
    ([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6), ([-1, -2, -3, -4, -5], -8),
])
def test_two_sum(nums, target):
    i, j = m.two_sum(nums, target)
    assert i != j and nums[i] + nums[j] == target


@pytest.mark.parametrize("nums,exp", [([1, 2, 3, 1], True), ([1, 2, 3, 4], False), ([], False), ([5], False)])
def test_contains_duplicate(nums, exp):
    assert m.contains_duplicate(nums) is exp


@pytest.mark.parametrize("s,t,exp", [("anagram", "nagaram", True), ("rat", "car", False), ("a", "ab", False), ("", "", True)])
def test_is_anagram(s, t, exp):
    assert m.is_anagram(s, t) is exp


def test_group_anagrams():
    res = m.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in res) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert sorted(sorted(g) for g in m.group_anagrams([""])) == [[""]]


@pytest.mark.parametrize("nums,k,exp", [([1, 1, 1, 2, 2, 3], 2, {1, 2}), ([1], 1, {1}), ([4, 4, 5, 5, 5, 6], 1, {5})])
def test_top_k_frequent(nums, k, exp):
    assert set(m.top_k_frequent(nums, k)) == exp


@pytest.mark.parametrize("nums,exp", [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]), ([2, 3], [3, 2])])
def test_product_except_self(nums, exp):
    assert m.product_except_self(nums) == exp


@pytest.mark.parametrize("nums,exp", [([100, 4, 200, 1, 3, 2], 4), ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9), ([], 0), ([1, 2, 0, 1], 3)])
def test_longest_consecutive(nums, exp):
    assert m.longest_consecutive(nums) == exp
