def merge_sorted(a, b):
    """Merge two ascending-sorted integer lists into one new ascending list.

    Duplicates are preserved and neither input list is modified.
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
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
