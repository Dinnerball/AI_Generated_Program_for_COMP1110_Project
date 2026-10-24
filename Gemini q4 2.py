def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    result = [0, 1]
    for _ in range(2, n):
        result.append(result[-1] + result[-2])
    return result[:n]

