def find_pairs(numbers, target):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    pairs = set()

    for num in counts:
        other = target - num

        if other not in counts:
            continue

        if num < other:
            pairs.add((num, other))
        elif num == other and counts[num] >= 2:
            pairs.add((num, num))

    return sorted(pairs)
