"""Q8: find all unique pairs of integers summing to a target.

This module provides :func:`find_pairs`. It never modifies the input list and
prints nothing. It is an independent alternative to the existing
``find_pairs.py``, ``q8_find_pairs.py`` and ``q8_solution.py`` in this folder,
which are left untouched.
"""


def find_pairs(numbers, target):
    """Return all unique pairs of integers from ``numbers`` summing to ``target``.

    Each pair must use two *different* positions of ``numbers``, so a value such
    as ``2`` pairs with itself only when it occurs at least twice. Inside every
    returned tuple the smaller number comes first, and the final list of tuples
    is sorted in ascending order with no duplicates.

    The input list is not modified and nothing is printed.

    Args:
        numbers: A sequence of integers.
        target: The required sum of each pair.

    Returns:
        A sorted list of ``(smaller, larger)`` tuples.
    """
    # A set gives free de-duplication of value pairs; iterating by index keeps
    # the two positions distinct, which is what allows a repeated value to pair
    # with itself. The caller's list is only ever read.
    found = set()
    length = len(numbers)

    for i in range(length):
        for j in range(i + 1, length):
            first = numbers[i]
            second = numbers[j]
            if first + second == target:
                found.add((first, second) if first <= second else (second, first))

    return sorted(found)


if __name__ == "__main__":
    # Self-checks; they raise on failure and print nothing.
    assert find_pairs([1, 2, 3, 4, 3], 5) == [(1, 4), (2, 3)]
    assert find_pairs([2, 2, 2], 4) == [(2, 2)]
    assert find_pairs([2], 4) == []
    assert find_pairs([], 0) == []
    assert find_pairs([5, 5], 10) == [(5, 5)]
    assert find_pairs([-1, 0, 1, 2], 1) == [(-1, 2), (0, 1)]
    assert find_pairs([3, 1, 2, 2], 4) == [(1, 3), (2, 2)]
    assert find_pairs([1, 2, 3], 100) == []

    original = [1, 2, 3, 4]
    find_pairs(original, 5)
    assert original == [1, 2, 3, 4]
