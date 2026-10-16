"""Q7: merge two ascending-sorted integer lists into one new ascending list.

merge_sorted(a, b) -> list
  * `a` and `b` are each already sorted in ascending order;
  * the returned list is new and contains every element of both inputs;
  * duplicates are preserved exactly as many times as they occur;
  * neither input list is modified;
  * nothing is printed.

Approach: a single two-pointer sweep.  Both fronts are already sorted, so
the next output element is always the smaller of the two current fronts.
Once one input is exhausted, the remaining tail of the other is already in
order and can be copied directly.  Total work is O(len(a) + len(b)) time and
O(len(a) + len(b)) space for the result.
"""


def merge_sorted(a, b):
    """Return a new ascending-sorted list holding all elements of `a` and `b`.

    Both inputs must already be sorted in ascending order.  Duplicate values
    are kept, and both input lists are left unchanged.

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
    i = 0                  # next unconsumed index in a
    j = 0                  # next unconsumed index in b
    len_a = len(a)
    len_b = len(b)

    # "<=" consumes from `a` first on ties; that keeps duplicates and gives
    # a stable a-before-b ordering for equal values.
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # At most one input still has a tail left; it is already sorted, and
    # slicing builds new list objects so the inputs themselves are untouched.
    if i < len_a:
        result.extend(a[i:])
    if j < len_b:
        result.extend(b[j:])

    return result


if __name__ == "__main__":
    # Silent self-check: assertions only, so nothing is ever printed.
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([1, 2, 2, 3], [2, 3, 4]) == [1, 2, 2, 2, 3, 3, 4]
    assert merge_sorted([], [1, 1]) == [1, 1]
    assert merge_sorted([5], []) == [5]
    assert merge_sorted([], []) == []
    assert merge_sorted([-3, 0, 7], [-5, 0, 7, 9]) == [-5, -3, 0, 0, 7, 7, 9]
    assert merge_sorted([2, 2, 2], [2, 2]) == [2, 2, 2, 2, 2]

    # Fresh-list and no-mutation guarantees.
    x = [1, 4]
    y = [2, 3]
    out = merge_sorted(x, y)
    assert out == [1, 2, 3, 4]
    assert out is not x and out is not y
    assert x == [1, 4] and y == [2, 3]
