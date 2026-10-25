import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("nums,exp", [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1)])
def test_single_number(nums, exp):
    assert m.single_number(nums) == exp


@pytest.mark.parametrize("n,exp", [(11, 3), (128, 1), (2 ** 31 - 1, 31), (0, 0)])
def test_hamming_weight(n, exp):
    assert m.hamming_weight(n) == exp


@pytest.mark.parametrize("n,exp", [(2, [0, 1, 1]), (5, [0, 1, 1, 2, 1, 2]), (0, [0])])
def test_count_bits(n, exp):
    assert m.count_bits(n) == exp


@pytest.mark.parametrize("nums,exp", [([3, 0, 1], 2), ([0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)])
def test_missing_number(nums, exp):
    assert m.missing_number(nums) == exp


@pytest.mark.parametrize("n,exp", [(1, True), (16, True), (18, False), (0, False), (-8, False), (2 ** 30, True)])
def test_is_power_of_two(n, exp):
    assert m.is_power_of_two(n) is exp


@pytest.mark.parametrize("n,exp", [(43261596, 964176192), (4294967293, 3221225471), (0, 0)])
def test_reverse_bits(n, exp):
    assert m.reverse_bits(n) == exp


@pytest.mark.parametrize("n,exp", [(0, 0), (1, 0), (2, 0), (3, 1), (10, 4), (100, 25), (1_000_000, 78498)])
def test_count_primes(n, exp):
    assert m.count_primes(n) == exp


@pytest.mark.parametrize("a,b,exp", [(48, 18, 6), (7, 13, 1), (0, 5, 5), (100, 100, 100)])
def test_gcd(a, b, exp):
    assert m.gcd(a, b) == exp


@pytest.mark.parametrize("b,e,mod", [(2, 10, 1000), (3, 200, 13), (7, 0, 5), (123456789, 987654321, 1_000_000_007)])
def test_fast_pow(b, e, mod):
    assert m.fast_pow(b, e, mod) == pow(b, e, mod)
