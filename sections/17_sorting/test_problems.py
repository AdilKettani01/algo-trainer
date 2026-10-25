import random
import pytest
from helpers import load

m = load(__file__)
rng = random.Random(42)
CASES = [[], [1], [2, 1], [3, 3, 3], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [-1, 5, -3, 0, 5, 2]] + \
        [[rng.randint(-50, 50) for _ in range(rng.randint(2, 200))] for _ in range(8)]


@pytest.mark.parametrize("nums", CASES)
def test_merge_sort(nums):
    assert m.merge_sort(list(nums)) == sorted(nums)


@pytest.mark.parametrize("nums", CASES)
def test_quick_sort(nums):
    assert m.quick_sort(list(nums)) == sorted(nums)


@pytest.mark.parametrize("nums", CASES)
def test_heap_sort(nums):
    assert m.heap_sort(list(nums)) == sorted(nums)


@pytest.mark.parametrize("nums", [c for c in CASES if c])
def test_quickselect(nums):
    s = sorted(nums)
    for k in {1, len(nums), (len(nums) + 1) // 2}:
        assert m.quickselect(list(nums), k) == s[k - 1]


@pytest.mark.parametrize("nums", [[2, 0, 2, 1, 1, 0], [2, 0, 1], [0], [1, 1], [2, 2, 2, 0, 0], []])
def test_sort_colors(nums):
    a = list(nums)
    m.sort_colors(a)
    assert a == sorted(nums)


@pytest.mark.parametrize("nums,exp", [([2, 4, 1, 3, 5], 3), ([5, 4, 3, 2, 1], 10), ([1, 2, 3], 0), ([], 0), ([2, 2, 2], 0)])
def test_count_inversions(nums, exp):
    assert m.count_inversions(nums) == exp
