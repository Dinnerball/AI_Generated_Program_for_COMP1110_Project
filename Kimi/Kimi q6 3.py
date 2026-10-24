def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True          # 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:        # only check divisors up to sqrt(n)
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6               # 6k ± 1 optimization
    return True
