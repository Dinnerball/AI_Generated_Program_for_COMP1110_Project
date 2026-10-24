"""Q7: merge two ascending-sorted lists of integers into one new sorted list.

merge_sorted(a, b) returns a new list containing every element of a and b in
ascending order. Duplicates are preserved, neither input list is modified, and
nothing is printed.
"""


def merge_sorted(a, b):
    """Return a new ascending-sorted list with all elements of a and b.

    Both ``a`` and ``b`` are assumed to already be sorted in non-decreasing
    order. Duplicate values are kept, and neither input list is mutated.
    """
    merged = []
    i = 0
    j = 0
    len_a = len(a)
    len_b = len(b)

    # Always take the smaller of the two current front elements.
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # One list is exhausted; copy the remainder of the other.
    if i < len_a:
        merged.extend(a[i:])
    if j < len_b:
        merged.extend(b[j:])

    return merged


if __name__ == "__main__":
    # Quiet self-check: asserts only, no output.
    xs = [1, 3, 3, 7]
    ys = [2, 3, 8]
    xs_copy = list(xs)
    ys_copy = list(ys)

    assert merge_sorted(xs, ys) == [1, 2, 3, 3, 3, 7, 8]
    assert xs == xs_copy and ys == ys_copy          # inputs untouched
    assert merge_sorted([], []) == []
    assert merge_sorted([], [1, 2]) == [1, 2]
    assert merge_sorted([4, 4], []) == [4, 4]
    assert merge_sorted([-5, -1], [-3, 0]) == [-5, -3, -1, 0]
    assert merge_sorted([5], [1, 2, 3]) == [1, 2, 3, 5]
    assert merge_sorted([1, 1, 1], [1, 1]) == [1, 1, 1, 1, 1]
