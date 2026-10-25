'Section 16 - Bit Manipulation & Math (your workspace).'


from typing import List


def single_number(nums: List[int]) -> int:
    """Every value appears twice except one. Find it.

    single_number([4,1,2,1,2]) -> 4
    Target: O(n) time, O(1) space. a ^ a = 0 and a ^ 0 = a.
    """
    pass


def hamming_weight(n: int) -> int:
    """Count the 1-bits in a non-negative integer.

    hamming_weight(11) -> 3   (1011)
    Target: O(number of set bits). n & (n-1) clears the lowest set bit.
    """
    pass


def count_bits(n: int) -> List[int]:
    """Return a list ans[0..n] where ans[i] = number of 1-bits in i.

    count_bits(5) -> [0,1,1,2,1,2]
    Target: O(n). ans[i] = ans[i >> 1] + (i & 1).
    """
    pass


def missing_number(nums: List[int]) -> int:
    """nums holds n distinct numbers from 0..n. Return the one missing.

    missing_number([3,0,1]) -> 2
    Target: O(n) time, O(1) space.
    """
    pass


def is_power_of_two(n: int) -> bool:
    """True if n == 2^k for some k >= 0.

    is_power_of_two(16) -> True ; is_power_of_two(18) -> False
    Target: O(1). A power of two has exactly one set bit.
    """
    pass


def reverse_bits(n: int) -> int:
    """Reverse the bits of a 32-bit unsigned integer.

    reverse_bits(43261596) -> 964176192
    Target: O(32).
    """
    pass


def count_primes(n: int) -> int:
    """Number of primes strictly less than n.

    count_primes(10) -> 4   (2,3,5,7)
    Target: O(n log log n) - Sieve of Eratosthenes.
    """
    pass


def gcd(a: int, b: int) -> int:
    """Greatest common divisor (Euclid's algorithm). Don't use math.gcd.

    gcd(48, 18) -> 6
    Target: O(log min(a, b)).
    """
    pass


def fast_pow(base: int, exp: int, mod: int) -> int:
    """(base ** exp) % mod using exponentiation by squaring. Don't use pow(a, b, c).

    fast_pow(2, 10, 1000) -> 24
    Target: O(log exp).
    """
    pass
