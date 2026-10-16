"""COMP1110 Q8 - find_pairs.

Returns all unique pairs of integers from the list whose sum equals target.
"""


def find_pairs(numbers, target):
    """Return sorted unique pairs (smaller first) summing to target.

    Each pair uses two different positions in ``numbers``, so the same
    position can never be used twice (even when the value appears once).
    The input list is not modified.
    """
    counts = {}
    for value in numbers:
        counts[value] = counts.get(value, 0) + 1

    seen = set()
    for value in counts:
        complement = target - value
        if complement not in counts:
            continue
        if complement == value and counts[value] < 2:
            continue  # need two distinct positions with the same value
        low, high = (value, complement) if value <= complement else (complement, value)
        seen.add((low, high))

    return sorted(seen)
