"""Q8: find all unique pairs of integers summing to a target.

This module provides :func:`find_pairs`. It never modifies the input list and
never prints anything.

It is a new, independent file. The programs already present in this folder
(``find_pairs.py``, ``q8_find_pairs.py``, ``q8_find_pairs_v2.py``,
``q8_find_pairs_v3.py`` and ``q8_solution.py``) are left exactly as they were.
"""

from collections import Counter


def find_pairs(numbers, target):
    """Return all unique pairs of integers from ``numbers`` summing to ``target``.

    Each pair must use two *different* positions of ``numbers``, so a value such
    as ``2`` pairs with itself only when it occurs at least twice. Inside every
    returned tuple the smaller number comes first, and the final list of tuples
    is sorted in ascending order with no duplicate pairs.

    The input list is not modified and nothing is printed.

    Args:
        numbers: A list (or other iterable) of integers.
        target: The required sum of each returned pair.

    Returns:
        A sorted list of ``(smaller, larger)`` tuples, possibly empty.

    Examples:
        >>> find_pairs([1, 2, 3, 4, 3], 5)
        [(1, 4), (2, 3)]
        >>> find_pairs([2, 2, 2], 4)
        [(2, 2)]
        >>> find_pairs([1, 2, 3], 100)
        []
    """
    # Count how often each value occurs, so the two-different-positions rule
    # becomes a counting rule: a pair (a, b) with a != b is allowed when both
    # values exist, and a pair (a, a) is allowed only when a occurs at least
    # twice. Working on a copy of the counts leaves the input untouched, and
    # values are only ever read, never mutated.
    counts = Counter(numbers)
    pairs = set()

    for value in counts:
        complement = target - value
        if complement not in counts:
            continue
        if complement > value:
            # Each distinct value pair is discovered from its smaller element
            # only, which keeps the result free of duplicates.
            pairs.add((value, complement))
        elif complement == value and counts[value] >= 2:
            pairs.add((value, value))

    return sorted(pairs)


if __name__ == "__main__":
    # Self-checks: these raise on failure and print nothing.
    assert find_pairs([1, 2, 3, 4, 3], 5) == [(1, 4), (2, 3)]
    assert find_pairs([2, 2, 2], 4) == [(2, 2)]
    assert find_pairs([2], 4) == []
    assert find_pairs([], 0) == []
    assert find_pairs([5, 5], 10) == [(5, 5)]
    assert find_pairs([5], 10) == []
    assert find_pairs([-1, 0, 1, 2], 1) == [(-1, 2), (0, 1)]
    assert find_pairs([3, 1, 2, 2], 4) == [(1, 3), (2, 2)]
    assert find_pairs([1, 2, 3], 100) == []
    assert find_pairs([0, 0, 0], 0) == [(0, 0)]
    assert find_pairs([4, 4, 4, 1], 5) == [(1, 4)]
    assert find_pairs([-3, -3, 6], 3) == [(-3, 6)]

    original = [1, 2, 3, 4]
    find_pairs(original, 5)
    assert original == [1, 2, 3, 4]
