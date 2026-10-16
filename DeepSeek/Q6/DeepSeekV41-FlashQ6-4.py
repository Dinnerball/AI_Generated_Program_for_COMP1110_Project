"""Q6: primality test.

is_prime(n) returns True if n is prime, False otherwise.
Handles negatives, 0 and 1 correctly, and prints nothing.
"""


def is_prime(n):
    """Return True if n is a prime number, False otherwise.

    A prime is an integer greater than 1 whose only positive divisors
    are 1 and itself. Non-integers, negatives, 0 and 1 are not prime.
    """
    # Reject non-integers (e.g. floats, strings) and bool edge cases are
    # kept simple: integers only.
    if isinstance(n, bool) or not isinstance(n, int):
        return False

    # 2 and 3 are prime; anything <= 1 (negatives, 0, 1) is not.
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Multiples of 2 and 3 are composite.
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check candidate divisors of the form 6k +/- 1 up to sqrt(n).
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


if __name__ == "__main__":
    # Nothing is printed by is_prime itself; assertions verify behaviour.
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(97) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(100) is False
