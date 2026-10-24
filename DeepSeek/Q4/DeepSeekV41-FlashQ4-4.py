def fibonacci(n):
    """Return a list of the first n Fibonacci numbers, starting with 0 and 1.

    n is assumed to be a non-negative integer. If n is 0, an empty list is
    returned. Nothing is printed.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    # Quick self-check (no output when imported as a module).
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
