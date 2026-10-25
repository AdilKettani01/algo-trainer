import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("nums,exp", [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1), ([5, 4, -1, 7, 8], 23), ([-3, -1, -2], -1)])
def test_max_sub_array(nums, exp):
    assert m.max_sub_array(nums) == exp


@pytest.mark.parametrize("nums,exp", [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False), ([0], True), ([0, 1], False)])
def test_can_jump(nums, exp):
    assert m.can_jump(nums) is exp


@pytest.mark.parametrize("nums,exp", [([2, 3, 1, 1, 4], 2), ([2, 3, 0, 1, 4], 2), ([1], 0), ([1, 1, 1, 1], 3)])
def test_jump(nums, exp):
    assert m.jump(nums) == exp


@pytest.mark.parametrize("gas,cost,exp", [([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3), ([2, 3, 4], [3, 4, 3], -1), ([5], [4], 0)])
def test_can_complete_circuit(gas, cost, exp):
    assert m.can_complete_circuit(gas, cost) == exp


@pytest.mark.parametrize("s,exp", [("ababcbacadefegdehijhklij", [9, 7, 8]), ("eccbbbbdec", [10]), ("abc", [1, 1, 1])])
def test_partition_labels(s, exp):
    assert m.partition_labels(s) == exp


@pytest.mark.parametrize("iv,exp", [([[1, 2], [2, 3], [3, 4], [1, 3]], 1), ([[1, 2], [1, 2], [1, 2]], 2), ([[1, 2], [2, 3]], 0)])
def test_erase_overlap_intervals(iv, exp):
    assert m.erase_overlap_intervals([list(x) for x in iv]) == exp


@pytest.mark.parametrize("r,exp", [([1, 0, 2], 5), ([1, 2, 2], 4), ([1, 3, 2, 2, 1], 7), ([5], 1)])
def test_candy(r, exp):
    assert m.candy(r) == exp
