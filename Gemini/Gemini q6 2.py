def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    # 检查到平方根即可
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

