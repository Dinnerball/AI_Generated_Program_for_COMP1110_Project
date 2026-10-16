def find_pairs(numbers, target):
    """Return all unique pairs of integers from ``numbers`` summing to ``target``.

    Rules:
      * A pair must use two *different* positions of ``numbers``, so a value
        such as ``2`` can pair with itself only when it occurs at least twice.
      * Within a pair the smaller number comes first.
      * The returned list of tuples is sorted in ascending order and holds no
        duplicates, even if the input repeats values.
      * The input list is never modified and nothing is printed.

    Args:
        numbers: An iterable of integers.
        target: The required sum of each returned pair.

    Returns:
        A sorted list of ``(smaller, larger)`` tuples.
    """
    # Count occurrences (a separate dict keeps the caller's list untouched).
    counts = {}
    for value in numbers:
        counts[value] = counts.get(value, 0) + 1

    pairs = set()
    for value in counts:
        complement = target - value
        # Skip when the complement is absent, or when this ordered pair was
        # already produced by the complementary value.
        if complement not in counts or complement < value:
            continue
        # Same value on both sides of the pair needs two distinct positions.
        if complement == value and counts[value] < 2:
            continue
        pairs.add((value, complement))

    return sorted(pairs)
