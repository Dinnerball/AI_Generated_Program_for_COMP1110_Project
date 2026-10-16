"""Q6: primality test for an integer.

is_prime(n) -> bool

A prime number is an integer greater than 1 with no positive divisors
other than 1 and itself.
"""


def is_prime(n):
    """Return True if n is prime, False otherwise.

    Negative integers, 0 and 1 are not prime, so they return False.
    The function never prints anything.
    """
    # Anything that is not a plain integer (including bool) is not prime.
    if isinstance(n, bool) or not isinstance(n, int):
        return False

    # Handles every negative integer, 0 and 1.
    if n < 2:
        return False

    # 2 and 3 are prime.
    if n < 4:
        return True

    # Any other even number has 2 as a divisor.
    if n % 2 == 0:
        return False

    # Trial division by odd candidates up to sqrt(n).
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2

    return True


if __name__ == "__main__":
    # Assert-only self-check, so running the file prints nothing.
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(97) is True
    assert is_prime(7919) is True
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(100) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-1) is False
    assert is_prime(-7) is False
    assert is_prime(-100) is False
    assert is_prime(2.0) is False
    assert is_prime(True) is False
    assert is_prime("7") is False
