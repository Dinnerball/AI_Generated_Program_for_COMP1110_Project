"""Q6: primality test.

is_prime(n) returns True if the integer n is prime, False otherwise.
A prime is an integer greater than 1 whose only positive divisors are 1 and
itself, so 0, 1, and all negative integers are not prime.

This module prints nothing; it only returns a value.
"""


def is_prime(n):
    """Return True if n is a prime number, False otherwise.

    Handles n <= 1 (including 0 and negative integers) by returning False.
    The test runs in O(sqrt(n)) time by checking trial divisors up to the
    integer square root of n.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("is_prime() expects an integer")

    if n < 2:
        return False

    if n < 4:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6

    return True
