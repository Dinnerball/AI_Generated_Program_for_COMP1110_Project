"""Q6: primality test for an integer."""


def is_prime(n):
    """Return True if n is a prime number, False otherwise.

    A prime is an integer greater than 1 whose only positive divisors are
    1 and itself. Returns False for negative integers, 0 and 1.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        return False
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


if __name__ == "__main__":
    # Self-check: no output on import, and no printing anywhere above.
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False
    assert is_prime(97) is True
    assert is_prime(100) is False
    assert is_prime(7919) is True
