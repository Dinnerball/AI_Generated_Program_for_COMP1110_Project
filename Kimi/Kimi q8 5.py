def find_pairs(numbers, target):
    seen = {}          # value -> count of positions used
    pairs = set()
    for i, x in enumerate(numbers):
        y = target - x
        if seen.get(y, 0) > 0:
            # ensure two different positions: only pair if y appeared before
            pairs.add((min(x, y), max(x, y)))
        seen[x] = seen.get(x, 0) + 1
    return sorted(pairs)
