# 16 - Bit Manipulation & Number Theory

## Bit operators (Python ints are arbitrary precision)
`&` and · `|` or · `^` xor · `~` not · `<<` `>>` shifts.

| Trick | Expression |
|---|---|
| Test bit i | `(n >> i) & 1` |
| Set / clear / toggle bit i | `n \| (1<<i)` / `n & ~(1<<i)` / `n ^ (1<<i)` |
| Lowest set bit | `n & -n` |
| Clear lowest set bit | `n & (n-1)` |
| Power of two? | `n > 0 and n & (n-1) == 0` |
| Multiply / divide by 2ᵏ | `n << k` / `n >> k` |

## XOR properties
`a ^ a = 0`, `a ^ 0 = a`, commutative & associative → XOR of all elements cancels pairs: **single number** in O(1) space. Swap without temp: `a ^= b; b ^= a; a ^= b`.

## Counting bits
- Brian Kernighan: `while n: n &= n-1; count += 1` - loops once per set bit.
- DP: `bits[i] = bits[i >> 1] + (i & 1)`.

## Bitmask subsets
Represent a subset of `n ≤ 20` items as an integer: `for mask in range(1 << n)`. Basis of bitmask DP and fast subset sums.

## Number theory essentials
- **GCD (Euclid)**: `gcd(a, b) = gcd(b, a % b)`; `lcm = a * b // gcd`.
- **Sieve of Eratosthenes**: cross out multiples starting from `p²` → O(n log log n).
- **Fast exponentiation**: square the base, halve the exponent → O(log e). With modulus after every multiply.
- Modular arithmetic: `(a + b) % m`, `(a * b) % m`; division needs a modular inverse (`pow(b, m-2, m)` for prime m).
- Primality: trial division up to `√n`.
- Sum 1..n = `n(n+1)/2` → "missing number".

## Pitfalls
- Python's `~n` = `-n-1` and negative numbers have infinite sign bits - mask with `& 0xFFFFFFFF` to emulate 32-bit.
- Operator precedence: `n & 1 == 0` parses as `n & (1 == 0)` - use parentheses.

**Practice:** `single_number`, `hamming_weight`, `count_bits`, `missing_number`, `is_power_of_two`, `reverse_bits`, `count_primes`, `gcd`, `fast_pow`.
