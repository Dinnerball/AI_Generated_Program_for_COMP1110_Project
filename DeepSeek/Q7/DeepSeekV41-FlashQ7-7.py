"""Q7: merge two ascending-sorted integer lists into one new sorted list.

COMP1110 group project — Question 7.

Rules implemented:
  * both inputs are already sorted in ascending order;
  * the result is a brand-new list containing every element of both inputs;
  * duplicates are preserved (they are real elements, not errors);
  * neither input list is modified;
  * nothing is printed.

The algorithm is the standard two-pointer merge: advance whichever input
currently has the smaller next element, then drain whatever is left.  Because
each input is sorted, this yields a sorted output without any re-sorting, in
O(len(a) + len(b)) time and O(len(a) + len(b)) extra space for the result.
"""


def merge_sorted(a, b):
    """Return a new ascending-sorted list with all elements of ``a`` and ``b``.

    ``a`` and ``b`` must each already be sorted in ascending order.  Duplicate
    values are kept, and both inputs are left untouched.

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
    i = 0  # index into a
    j = 0  # index into b
    len_a = len(a)
    len_b = len(b)

    # Take the smaller front element; "<=" keeps duplicates and preserves the
    # relative order of equal values coming from a before those from b.
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # At most one of these loops actually runs; the other side is exhausted.
    if i < len_a:
        result.extend(a[i:])
    if j < len_b:
        result.extend(b[j:])

    return result


if __name__ == "__main__":
    # Self-check, kept quiet: nothing is printed, a failure raises.
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([1, 2, 2, 3], [2, 3, 4]) == [1, 2, 2, 2, 3, 3, 4]
    assert merge_sorted([], [1, 1]) == [1, 1]
    assert merge_sorted([5], []) == [5]
    assert merge_sorted([], []) == []
    assert merge_sorted([-3, 0, 7], [-5, 0, 7, 9]) == [-5, -3, 0, 0, 7, 7, 9]

    x = [1, 4]
    y = [2, 3]
    out = merge_sorted(x, y)
    assert out == [1, 2, 3, 4] and out is not x and out is not y
    assert x == [1, 4] and y == [2, 3]  # inputs untouched
