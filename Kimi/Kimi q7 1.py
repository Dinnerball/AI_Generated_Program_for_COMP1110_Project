def merge_sorted(a, b):
    """Merge two ascending-sorted lists into one new ascending-sorted list.

    Preserves duplicates and does not modify either input list.
    """
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # <= keeps it stable: equal elements from a come first
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
