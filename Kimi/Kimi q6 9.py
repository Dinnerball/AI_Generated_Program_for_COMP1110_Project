def is_prime(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return False
    if n < 2:
        return False
    if n < 4:  # 2 and 3
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
