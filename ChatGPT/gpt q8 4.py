def find_pairs(numbers, target):
    pairs = set()
    seen = {}

    for num in numbers:
        complement = target - num
        if complement in seen and seen[complement] > 0:
            pairs.add(tuple(sorted((num, complement))))
            seen[complement] -= 1
        else:
            seen[num] = seen.get(num, 0) + 1

    return sorted(pairs)