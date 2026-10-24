"""Q8: find unique pairs of integers summing to a target.

This module defines a single public function, ``find_pairs``. It does not
print anything and does not modify the input list.
"""


def find_pairs(numbers, target):
    """Return all unique pairs from ``numbers`` that sum to ``target``.

    A pair uses two *different positions* of ``numbers``, so an element may
    pair with an equal-valued element at another index (duplicates in the
    input can therefore matter), but no index is ever used twice.

    Each returned tuple holds the smaller value first, and the list of pairs
    is sorted in ascending order. Pairs are unique: the same unordered pair
    of values is reported only once, even when it is achievable through more
    than one combination of positions.

    ``numbers`` is never modified and nothing is printed.

    Args:
        numbers: An iterable of integers (not modified).
        target: The required sum of each pair.

    Returns:
        list[tuple[int, int]]: Sorted unique pairs, smaller value first.

    Examples:
        >>> find_pairs([1, 2, 3, 4, 5], 5)
        [(1, 4), (2, 3)]
        >>> find_pairs([1, 1, 1], 2)
        [(1, 1)]
        >>> find_pairs([1, 2, 3], 100)
        []
    """
    # Work on a local list so the caller's object is untouched.
    values = list(numbers)

    seen_pairs = set()
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            a, b = values[i], values[j]
            if a + b == target:
                # Order the two values, then let the set remove duplicates
                # coming from different index combinations.
                seen_pairs.add((a, b) if a <= b else (b, a))

    return sorted(seen_pairs)


if __name__ == "__main__":
    # Self-check only; the function itself never prints.
    assert find_pairs([1, 2, 3, 4, 5], 5) == [(1, 4), (2, 3)]
    assert find_pairs([1, 1, 1], 2) == [(1, 1)]
    assert find_pairs([1, 2, 3], 100) == []
    assert find_pairs([], 0) == []
    assert find_pairs([0], 0) == []
    assert find_pairs([0, 0], 0) == [(0, 0)]
    assert find_pairs([-3, 1, 4, 2, -1], 1) == [(-3, 4), (-1, 2)]
    assert find_pairs([5, 5, 5, 5], 10) == [(5, 5)]

    data = [3, 1, 2]
    find_pairs(data, 4)
    assert data == [3, 1, 2], "input list must not be modified"
    print("all self-checks passed")
