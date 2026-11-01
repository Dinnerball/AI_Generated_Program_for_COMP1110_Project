def fibonacci(n):
    if n == 0:
        return []
    
    fib = [0]
    if n == 1:
        return fib
    
    fib.append(1)
    
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    return fib
