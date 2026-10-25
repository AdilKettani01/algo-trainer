"""Section 16 - Bit Manipulation & Math (reference solutions)."""
from typing import List


def single_number(nums: List[int]) -> int:
    """Every value appears twice except one. Find it.

    single_number([4,1,2,1,2]) -> 4
    Target: O(n) time, O(1) space. a ^ a = 0 and a ^ 0 = a.
    """
    res = 0
    for x in nums:
        res ^= x
    return res


def hamming_weight(n: int) -> int:
    """Count the 1-bits in a non-negative integer.

    hamming_weight(11) -> 3   (1011)
    Target: O(number of set bits). n & (n-1) clears the lowest set bit.
    """
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def count_bits(n: int) -> List[int]:
    """Return a list ans[0..n] where ans[i] = number of 1-bits in i.

    count_bits(5) -> [0,1,1,2,1,2]
    Target: O(n). ans[i] = ans[i >> 1] + (i & 1).
    """
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


def missing_number(nums: List[int]) -> int:
    """nums holds n distinct numbers from 0..n. Return the one missing.

    missing_number([3,0,1]) -> 2
    Target: O(n) time, O(1) space.
    """
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


def is_power_of_two(n: int) -> bool:
    """True if n == 2^k for some k >= 0.

    is_power_of_two(16) -> True ; is_power_of_two(18) -> False
    Target: O(1). A power of two has exactly one set bit.
    """
    return n > 0 and n & (n - 1) == 0


def reverse_bits(n: int) -> int:
    """Reverse the bits of a 32-bit unsigned integer.

    reverse_bits(43261596) -> 964176192
    Target: O(32).
    """
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res


def count_primes(n: int) -> int:
    """Number of primes strictly less than n.

    count_primes(10) -> 4   (2,3,5,7)
    Target: O(n log log n) - Sieve of Eratosthenes.
    """
    if n < 3:
        return 0
    sieve = bytearray([1]) * n
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n, i)))  # cross out multiples
    return sum(sieve)


def gcd(a: int, b: int) -> int:
    """Greatest common divisor (Euclid's algorithm). Don't use math.gcd.

    gcd(48, 18) -> 6
    Target: O(log min(a, b)).
    """
    while b:
        a, b = b, a % b
    return a


def fast_pow(base: int, exp: int, mod: int) -> int:
    """(base ** exp) % mod using exponentiation by squaring. Don't use pow(a, b, c).

    fast_pow(2, 10, 1000) -> 24
    Target: O(log exp).
    """
    result, base = 1, base % mod
    while exp:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result % mod
