"""Q8: find all unique pairs of integers summing to a target.

This module provides :func:`find_pairs`. It never modifies the input list and
never prints anything.

It is a new, independent file: the other programs already in this folder
(``find_pairs.py``, ``q8_find_pairs.py``, ``q8_find_pairs_v2.py`` and
``q8_solution.py``) are left exactly as they were.
"""


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
    # Single pass over the values: for each value, a complement already stored
    # in ``seen`` must come from an earlier position, which is what guarantees
    # the two different positions. A value can therefore pair with itself only
    # when it has been seen before. The ``pairs`` set removes duplicate value
    # pairs, and the input is only ever read, never mutated.
    seen = set()
    pairs = set()

    for value in numbers:
        complement = target - value
        if complement in seen:
            pairs.add((complement, value) if complement <= value else (value, complement))
        seen.add(value)

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

    original = [1, 2, 3, 4]
    find_pairs(original, 5)
    assert original == [1, 2, 3, 4]
