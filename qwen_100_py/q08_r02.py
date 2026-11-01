def find_pairs(numbers, target):
    """
    Return all unique pairs of integers from numbers that sum to target.

    Each pair uses two different positions in the input list. The smaller
    number appears first in each tuple, and the returned list is sorted.
    """
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
