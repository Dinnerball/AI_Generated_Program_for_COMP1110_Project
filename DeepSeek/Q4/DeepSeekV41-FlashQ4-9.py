def fibonacci(n):
    """Return a list of the first n Fibonacci numbers, starting with 0 and 1.

    fibonacci(0) returns an empty list.
    """
    if n == 0:
        return []

    result = [0, 1]
    while len(result) < n:
        result.append(result[-1] + result[-2])
    return result[:n]
