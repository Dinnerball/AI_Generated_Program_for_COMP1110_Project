def find_pairs(numbers, target):
    """Return all unique pairs of integers from ``numbers`` that sum to ``target``.

    Each pair must come from two different positions in ``numbers``. Inside a
    pair the smaller number is placed first, and the returned list of tuples is
    sorted in ascending order.

    The input list is not modified and nothing is printed.

    Args:
        numbers: A sequence of integers.
        target: The required sum of each pair.

    Returns:
        A sorted list of tuples ``(smaller, larger)`` without duplicates.
    """
    pairs = set()
    length = len(numbers)

    for i in range(length):
        for j in range(i + 1, length):
            first = numbers[i]
            second = numbers[j]
            if first + second == target:
                pairs.add((first, second) if first <= second else (second, first))

    return sorted(pairs)
