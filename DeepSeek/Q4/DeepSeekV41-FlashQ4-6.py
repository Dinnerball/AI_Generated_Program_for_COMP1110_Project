def fibonacci(n):
    """Return a list of the first n Fibonacci numbers, starting with 0 and 1.

    If n is 0, return an empty list. Assumes n is a non-negative integer.
    """
    if n == 0:
        return []

    fibs = [0]
    a, b = 0, 1
    for _ in range(n - 1):
        fibs.append(b)
        a, b = b, a + b
    return fibs
