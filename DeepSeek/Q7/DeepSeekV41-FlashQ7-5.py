"""Q7: merge two ascending-sorted lists of integers into one new sorted list.

The function preserves duplicates and never modifies either input list.
"""


def merge_sorted(a, b):
    """Return a new ascending-sorted list containing all elements of a and b.

    Both ``a`` and ``b`` must already be sorted in non-decreasing order.
    Duplicates are preserved. Neither input list is modified.
    """
    merged = []
    i = 0
    j = 0
    len_a = len(a)
    len_b = len(b)

    # Walk both lists, always taking the smaller front element.
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Append whatever remains of either list.
    if i < len_a:
        merged.extend(a[i:])
    if j < len_b:
        merged.extend(b[j:])

    return merged
