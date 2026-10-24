def find_pairs(numbers, target):
    seen_values = set()
    pairs = set()
    for num in numbers:
        complement = target - num
        if complement in seen_values:
            pair = (complement, num) if complement < num else (num, complement)
            pairs.add(pair)
        seen_values.add(num)
    return sorted(list(pairs))

