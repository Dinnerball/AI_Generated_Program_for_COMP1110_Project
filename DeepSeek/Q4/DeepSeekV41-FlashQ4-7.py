def fibonacci(n):
    """Return a list of the first n Fibonacci numbers, starting with 0 and 1.

    n is assumed to be a non-negative integer. If n is 0, an empty list is
    returned. The function does not print anything.
    """
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
