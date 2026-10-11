def find_pairs(numbers, target):
    seen = set()
    pairs = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return sorted(pairs)
