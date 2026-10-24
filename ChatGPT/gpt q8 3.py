def find_pairs(numbers, target):
    pairs = set()
    seen = {}

    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            for _ in range(seen[complement]):
                pairs.add(tuple(sorted((num, complement))))
        seen[num] = seen.get(num, 0) + 1

    return sorted(pairs)