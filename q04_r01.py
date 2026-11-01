def fibonacci(n):
    if n == 0:
        return []
    
    fib_numbers = [0, 1]
    
    if n == 1:
        return [0]
    
    while len(fib_numbers) < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    
    return fib_numbers
