def find_pairs(numbers, target):
    seen = set()
    pairs = set()

    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)

    return sorted(pairs)