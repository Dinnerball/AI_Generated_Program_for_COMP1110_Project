def find_pairs(numbers, target):
    pairs = set()
    seen = set()
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return sorted(pairs)
