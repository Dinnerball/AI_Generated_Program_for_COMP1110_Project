def find_pairs(numbers, target):
    seen = {}          # value -> set of indices seen so far
    pairs = set()      # unique normalized pairs
    for i, x in enumerate(numbers):
        complement = target - x
        # any earlier index with the complement forms a valid pair
        if complement in seen and seen[complement]:
            pairs.add((min(x, complement), max(x, complement)))
        seen.setdefault(x, set()).add(i)
    return sorted(pairs)
