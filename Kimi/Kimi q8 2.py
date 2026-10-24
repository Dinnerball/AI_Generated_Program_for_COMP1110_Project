def find_pairs(numbers, target):
    seen = set()
    pairs = set()
    for i, x in enumerate(numbers):
        complement = target - x
        if complement in seen:
            pairs.add((min(x, complement), max(x, complement)))
        seen.add(x)
    return sorted(pairs)
