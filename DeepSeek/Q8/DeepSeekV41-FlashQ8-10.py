"""Q8: return all unique pairs of integers from a list that sum to a target.

The input list is never modified and nothing is printed on import.
"""


def find_pairs(numbers, target):
    """Return every unique pair from ``numbers`` whose sum equals ``target``.

    A pair must use two *different positions* of ``numbers``, so a value may be
    paired with itself only when it occurs at least twice (``[3, 3]`` with
    target ``6`` yields ``(3, 3)``, while ``[3]`` yields nothing).

    Each pair is returned as a tuple with the smaller number first, and the list
    of tuples is sorted in ascending order. Pairs are unique by value, so a
    repeated value contributes a given pair only once.

    Args:
        numbers: An iterable of integers.
        target: The required sum of each pair.

    Returns:
        A sorted list of tuples ``(smaller, larger)``; empty when no pair works.
    """
    values = list(numbers)          # local copy: the caller's list is untouched
    pairs = set()
    length = len(values)

    for i in range(length):
        for j in range(i + 1, length):          # j > i: two distinct positions
            first = values[i]
            second = values[j]
            if first + second == target:
                pairs.add((first, second) if first <= second else (second, first))

    return sorted(pairs)


def _demo():
    """Self-check that runs only when this file is executed directly."""
    assert find_pairs([1, 2, 3, 4, 5], 6) == [(1, 5), (2, 4)]
    assert find_pairs([2, 2, 2], 4) == [(2, 2)]
    assert find_pairs([3], 6) == []
    assert find_pairs([], 5) == []
    assert find_pairs([-1, 1, 2, -2, 0], 0) == [(-2, 2), (-1, 1)]
    assert find_pairs([1, 1, 2], 3) == [(1, 2)]
    assert find_pairs([4, 4, 4, 4], 8) == [(4, 4)]
    assert find_pairs([0, 5, 5, 0], 5) == [(0, 5)]

    data = [3, 1, 2]
    assert find_pairs(data, 4) == [(1, 3)]
    assert data == [3, 1, 2]                    # input list untouched


if __name__ == "__main__":
    _demo()
