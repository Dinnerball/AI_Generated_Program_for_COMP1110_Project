def find_pairs(numbers, target):
    pairs = set()
    seen = {}

    for i, num in enumerate(numbers):
        complement = target - num

        if complement in seen:
            for _ in seen[complement]:
                pair = (min(num, complement), max(num, complement))
                pairs.add(pair)

        seen.setdefault(num, []).append(i)
