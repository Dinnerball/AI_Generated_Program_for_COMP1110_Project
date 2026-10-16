"""Q8: find all unique pairs of integers summing to a target value."""

from collections import Counter
from typing import Iterable, List, Tuple


def find_pairs(numbers: Iterable[int], target: int) -> List[Tuple[int, int]]:
    """Return every unique pair of integers from ``numbers`` summing to ``target``.

    A pair may only use two *different positions* of the input sequence, so a
    value can be paired with itself only when it occurs at least twice
    (e.g. ``[3, 3]`` with target ``6`` gives ``(3, 3)``, but ``[3]`` gives
    nothing).

    Each returned tuple has the smaller value first, and the list of tuples is
    sorted in ascending order. Pairs are unique by value, so a repeated value
    contributes each matching pair only once. The input is never modified and
    nothing is printed.
    """
    counts = Counter(numbers)
    pairs = []

    for value in counts:
        complement = target - value
        if complement not in counts:
            continue
        if value < complement:
            pairs.append((value, complement))
        elif value == complement and counts[value] >= 2:
            pairs.append((value, value))

    pairs.sort()
    return pairs


def _demo() -> None:
    """Small self-check; runs only when this file is executed directly."""
    assert find_pairs([1, 2, 3, 4, 5], 6) == [(1, 5), (2, 4)]
    assert find_pairs([2, 2, 2], 4) == [(2, 2)]
    assert find_pairs([3], 6) == []
    assert find_pairs([-1, 1, 2, -2, 0], 0) == [(-2, 2), (-1, 1)]
    assert find_pairs([1, 1, 2], 3) == [(1, 2)]
    assert find_pairs([], 5) == []

    data = [3, 1, 2]
    print(find_pairs(data, 4))
    assert data == [3, 1, 2]  # input untouched


if __name__ == "__main__":
    _demo()
