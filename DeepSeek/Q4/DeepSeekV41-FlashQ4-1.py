def fibonacci(n):
    """Return a list of the first n Fibonacci numbers, starting with 0 and 1.

    If n is 0, an empty list is returned. n is assumed to be a
    non-negative integer. Nothing is printed.
    """
    if n <= 0:
        return []

    sequence = [0]
    a, b = 0, 1
    for _ in range(n - 1):
        sequence.append(b)
        a, b = b, a + b
    return sequence
