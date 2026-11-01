def find_pairs(numbers, target):
    seen = set()
    pairs = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            if num <= complement:
                pairs.add((num, complement))
            else:
                pairs.add((complement, num))
        seen.add(num)

    return sorted(pairs)
