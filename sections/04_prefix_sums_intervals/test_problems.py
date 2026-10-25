import pytest
from helpers import load

m = load(__file__)


def test_num_array():
    na = m.NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sum_range(0, 2) == 1
    assert na.sum_range(2, 5) == -1
    assert na.sum_range(0, 5) == -3
    assert na.sum_range(3, 3) == -5


@pytest.mark.parametrize("nums,k,exp", [([1, 1, 1], 2, 2), ([1, 2, 3], 3, 2), ([1, -1, 0], 0, 3), ([1], 0, 0)])
def test_subarray_sum(nums, k, exp):
    assert m.subarray_sum(nums, k) == exp


@pytest.mark.parametrize("nums,exp", [([0, 1], 2), ([0, 1, 0], 2), ([0, 0, 1, 0, 0, 0, 1, 1], 6), ([1, 1], 0)])
def test_find_max_length(nums, exp):
    assert m.find_max_length(nums) == exp


@pytest.mark.parametrize("iv,exp", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]), ([[1, 4], [0, 4]], [[0, 4]]), ([[1, 4], [2, 3]], [[1, 4]]),
])
def test_merge(iv, exp):
    assert m.merge([list(x) for x in iv]) == exp


@pytest.mark.parametrize("iv,exp", [([[0, 30], [5, 10], [15, 20]], 2), ([[7, 10], [2, 4]], 1), ([[1, 5], [5, 8]], 1), ([], 0)])
def test_min_meeting_rooms(iv, exp):
    assert m.min_meeting_rooms(iv) == exp
