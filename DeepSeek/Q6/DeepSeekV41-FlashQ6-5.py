"""Primality test utility.

Contains a single public function, :func:`is_prime`, which decides whether an
integer is a prime number. The function never prints anything; it only returns
a boolean.
"""

from math import isqrt

__all__ = ["is_prime"]


def is_prime(n):
    """Return True if ``n`` is a prime number, otherwise return False.

    A prime number is an integer greater than 1 that has no positive divisors
    other than 1 and itself. Consequently:

    * 0 ``->`` False (not greater than 1)
    * 1 ``->`` False (not greater than 1)
    * negative integers ``->`` False (not greater than 1)
    * 2 and 3 ``->`` True
    * any other even integer ``->`` False

    ``bool`` is a subclass of ``int`` in Python, so ``True`` and ``False`` would
    otherwise be treated as 1 and 0; they are explicitly rejected here.

    The search for divisors only needs to test candidates up to ``sqrt(n)``:
    if ``n = a * b`` with ``1 < a <= b``, then ``a <= sqrt(n)``. After checking
    2, only odd candidates are tested, which halves the remaining work.

    Parameters
    ----------
    n : int
        The value to test.

    Returns
    -------
    bool
        True if ``n`` is prime, False otherwise (including for non-integers).
    """
    # bool is a subclass of int; reject it along with every non-integer type.
    if isinstance(n, bool) or not isinstance(n, int):
        return False

    # 0, 1, and all negative integers are not prime.
    if n < 2:
        return False

    # 2 is the only even prime; every other even number is composite.
    if n < 4:
        return True
    if n % 2 == 0:
        return False

    # Test odd divisors from 3 up to and including sqrt(n).
    limit = isqrt(n)
    divisor = 3
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 2

    return True
