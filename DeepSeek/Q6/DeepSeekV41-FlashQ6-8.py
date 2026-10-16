"""Q6: primality test.

is_prime(n) -> True if n is prime, False otherwise.

A prime is an integer greater than 1 whose only positive divisors are
1 and itself.  So 0, 1 and every negative integer are not prime.
"""


def is_prime(n):
    """Return True if the integer n is prime, False otherwise.

    Handles negative integers and zero correctly (both are not prime),
    and never prints anything.
    """
    # Reject non-integers (e.g. floats, strings) without raising.
    if not isinstance(n, int) or isinstance(n, bool):
        return False

    # Primes must be greater than 1: this covers 0, 1 and all negatives.
    if n <= 1:
        return False

    if n <= 3:          # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # All primes > 3 are of the form 6k +/- 1, so only test those divisors.
    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True
