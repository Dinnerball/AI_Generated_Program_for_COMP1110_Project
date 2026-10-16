"""Q8: find all unique pairs of integers summing to a target.

This module provides :func:`find_pairs`. It never modifies the input list and
never prints anything.

This is a brand-new, independent file. Everything already in this folder
(``find_pairs.py``, ``q8_find_pairs.py``, ``q8_find_pairs_v2.py``,
``q8_find_pairs_v3.py``, ``q8_find_pairs_v4.py`` and ``q8_solution.py``) is
left completely untouched.
"""


def find_pairs(numbers, target):
    """Return all unique pairs of integers from ``numbers`` summing to ``target``.

    Each pair must occupy two *different* positions of ``numbers``, so a value
    such as ``2`` may pair with itself only when it appears at least twice.
    Within every returned tuple the smaller number comes first, and the final
    list of tuples is sorted in ascending order with no duplicate pairs.

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
    # Sorting a *copy* keeps the caller's list untouched. Two pointers from the
    # ends then walk inwards: when the current sum is too small the left pointer
    # moves up, when it is too large the right pointer moves down, and equal
    # values are skipped so each distinct pair is recorded only once. Pairing a
    # value with itself is naturally allowed when it occurs twice, because the
    # two pointers then sit on two different positions.
    ordered = sorted(numbers)
    pairs = []
    left, right = 0, len(ordered) - 1

    while left < right:
        total = ordered[left] + ordered[right]

        if total == target:
            pairs.append((ordered[left], ordered[right]))
            left += 1
            right -= 1
            # Skip repeated values on both sides to avoid duplicate pairs.
            while left < right and ordered[left] == ordered[left - 1]:
                left += 1
            while left < right and ordered[right] == ordered[right + 1]:
                right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1

    return pairs


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
    assert find_pairs([1, 1, 1, 1], 2) == [(1, 1)]
    assert find_pairs([-2, -1, 0, 1, 2], 0) == [(-2, 2), (-1, 1)]

    original = [1, 2, 3, 4]
    find_pairs(original, 5)
    assert original == [1, 2, 3, 4]
