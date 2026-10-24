def find_pairs(numbers, target):
    seen = {}
    for i, n in enumerate(numbers):
        seen.setdefault(n, []).append(i)

    pairs = set()
    for i, n in enumerate(numbers):
        complement = target - n
        if complement in seen:
            for j in seen[complement]:
                if j != i:
                    pairs.add((min(n, complement), max(n, complement)))
    return sorted(pairs)
