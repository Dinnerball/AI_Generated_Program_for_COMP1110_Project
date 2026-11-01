def fibonacci(n):
    if n == 0:
        return []
    
    fib = [0, 1]
    
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    
    return fib[:n]
