"""Q7: merge two ascending-sorted integer lists into one ascending list."""


def merge_sorted(a, b):
    """Return a new ascending-sorted list with all elements of a and b.

    a and b must each already be sorted in ascending order.
    Duplicate values are preserved; neither input list is modified.
    """
    merged = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Append whatever is left of whichever list still has elements.
    if i < len(a):
        merged.extend(a[i:])
    if j < len(b):
        merged.extend(b[j:])

    return merged
