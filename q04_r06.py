def fibonacci(n):
    if n == 0:
        return []

    fib = [0, 1]

    if n == 1:
        return [0]
    if n == 2:
        return fib

    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])

    return fib
