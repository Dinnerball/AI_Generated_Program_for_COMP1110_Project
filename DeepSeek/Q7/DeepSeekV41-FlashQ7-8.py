"""Q7: merge two ascending-sorted integer lists into one new sorted list.

merge_sorted(a, b) -> list
  * `a` and `b` are each already sorted in ascending order;
  * the returned list is new and holds every element of both inputs;
  * duplicates are preserved exactly as often as they occur;
  * neither input list is modified;
  * nothing is printed.

This is the standard two-pointer merge: repeatedly take the smaller of the two
current front elements, then drain whichever input still has elements left.
Because both inputs are sorted, the output comes out sorted with no re-sorting,
in O(len(a) + len(b)) time and O(len(a) + len(b)) space for the new list.
"""


def merge_sorted(a, b):
    """Return a new ascending-sorted list holding all elements of `a` and `b`.

    Both inputs must already be sorted in ascending order.  Duplicate values
    are kept, and both inputs are left unchanged.

    >>> merge_sorted([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge_sorted([1, 2, 2, 3], [2, 3, 4])
    [1, 2, 2, 2, 3, 3, 4]
    >>> merge_sorted([], [1, 1])
    [1, 1]
    >>> merge_sorted([5], [])
    [5]
    >>> merge_sorted([], [])
    []
    """
    result = []
    i = 0                  # index into a
    j = 0                  # index into b
    len_a = len(a)
    len_b = len(b)

    # "<=" takes from `a` first when the fronts are equal, which keeps every
    # duplicate value (and a stable a-before-b order for ties).
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # At most one of these two branches still has anything to copy.
    if i < len_a:
        result.extend(a[i:])
    if j < len_b:
        result.extend(b[j:])

    return result


def _main():
    """Silent self-check: a failure raises, nothing is ever printed."""
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([1, 2, 2, 3], [2, 3, 4]) == [1, 2, 2, 2, 3, 3, 4]
    assert merge_sorted([], [1, 1]) == [1, 1]
    assert merge_sorted([5], []) == [5]
    assert merge_sorted([], []) == []
    assert merge_sorted([-3, 0, 7], [-5, 0, 7, 9]) == [-5, -3, 0, 0, 7, 7, 9]
    assert merge_sorted([2, 2, 2], [2, 2]) == [2, 2, 2, 2, 2]

    x = [1, 4]
    y = [2, 3]
    out = merge_sorted(x, y)
    assert out == [1, 2, 3, 4]
    assert out is not x and out is not y       # a brand-new list
    assert x == [1, 4] and y == [2, 3]         # inputs untouched


if __name__ == "__main__":
    _main()
