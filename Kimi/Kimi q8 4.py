def find_pairs(numbers, target):
    seen = {}
    pairs = set()
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            # ensure different positions: complement index != i
            for j in seen[complement]:
                if j != i:
                    pairs.add((min(num, complement), max(num, complement)))
        seen.setdefault(num, []).append(i)
    return sorted(pairs)
