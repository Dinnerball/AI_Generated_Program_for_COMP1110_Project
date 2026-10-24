"""Prime test utility (Q6).

Provides :func:`is_prime`, which decides primality without printing anything.
"""

from math import isqrt

__all__ = ["is_prime"]


def is_prime(n):
    """Return True if ``n`` is a prime number, otherwise return False.

    A prime is an integer greater than 1 whose only positive divisors are
    1 and itself.  Negative integers, 0 and 1 are therefore not prime.

    Args:
        n: The integer to test.

    Returns:
        bool: True when ``n`` is prime, False otherwise.

    Raises:
        TypeError: If ``n`` is not an integer.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(1)
        False
        >>> is_prime(0)
        False
        >>> is_prime(-7)
        False
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("is_prime() requires an integer argument")

    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Every prime greater than 3 is of the form 6k +/- 1, so only those
    # candidates need to be tried as divisors up to sqrt(n).
    divisor = 5
    step = 2
    limit = isqrt(n)
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += step
        step = 6 - step

    return True
