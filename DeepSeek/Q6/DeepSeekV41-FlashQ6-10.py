"""Primeness test for an integer.

is_prime(n) -> True if n is prime, False otherwise.
A prime is an integer greater than 1 whose only positive divisors are 1 and itself,
so all negative integers, 0 and 1 are not prime.
"""


def is_prime(n):
    """Return True if n is a prime number, False otherwise.

    Handles negative integers and zero correctly (both are not prime).
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("is_prime() requires an integer argument")
    if n < 2:
        return False
    if n < 4:
        return True            # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:          # trial division by 6k +/- 1
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True
