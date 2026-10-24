def fibonacci(n):
    """Return a list of the first n Fibonacci numbers, starting with 0 and 1."""
    if n == 0:
        return []
    if n == 1:
        return [0]

    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
