def fibonacci(n):
    if n == 0:
        return []

    fib = [0]

    if n == 1:
        return fib

    fib.append(1)

    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    return fib
