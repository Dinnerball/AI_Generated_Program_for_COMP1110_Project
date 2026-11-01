def find_pairs(numbers, target):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    pairs = []
    for num in counts:
        complement = target - num

        if num <= complement and complement in counts:
            if num != complement or counts[num] >= 2:
                pairs.append((num, complement))

    return sorted(pairs)
