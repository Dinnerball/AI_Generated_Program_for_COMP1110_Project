def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

