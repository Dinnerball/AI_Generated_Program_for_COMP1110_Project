"""Merge two ascending-sorted integer lists into one new sorted list.

merge_sorted(a, b) -> list
  * `a` and `b` are each already sorted in ascending order;
  * the result is a brand-new list holding every element of both inputs;
  * duplicate values are preserved;
  * neither input list is modified;
  * nothing is printed.

Two-pointer merge: repeatedly take the smaller of the two front elements, then
drain whichever input still has elements.  Since both inputs are already
sorted, the output is sorted with no re-sorting, in O(len(a) + len(b)) time.
"""


def merge_sorted(a, b):
    """Return a new ascending-sorted list with all elements of `a` and `b`.

    Both inputs must already be sorted in ascending order.  Duplicates are
    kept, and both inputs are left unchanged.

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
    i = 0
    j = 0
    len_a = len(a)
    len_b = len(b)

    # "<=" takes from `a` first on ties, which preserves duplicate values.
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # At most one of these two has anything left to copy.
    if i < len_a:
        result.extend(a[i:])
    if j < len_b:
        result.extend(b[j:])

    return result


if __name__ == "__main__":
    # Silent self-check: a failure raises, nothing is printed.
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([1, 2, 2, 3], [2, 3, 4]) == [1, 2, 2, 2, 3, 3, 4]
    assert merge_sorted([], [1, 1]) == [1, 1]
    assert merge_sorted([5], []) == [5]
    assert merge_sorted([], []) == []
    assert merge_sorted([-3, 0, 7], [-5, 0, 7, 9]) == [-5, -3, 0, 0, 7, 7, 9]

    x = [1, 4]
    y = [2, 3]
    out = merge_sorted(x, y)
    assert out == [1, 2, 3, 4]
    assert out is not x and out is not y
    assert x == [1, 4] and y == [2, 3]
