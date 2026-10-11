def find_pairs(numbers, target):
    seen_pairs = set()
    result = set()
    for num in numbers:
        complement = target - num
        if complement in seen_pairs:
            result.add((min(num, complement), max(num, complement)))
        seen_pairs.add(num)
    return sorted(result)
