def merge_sorted(a, b):
    result = []
    i = j = 0
    len_a, len_b = len(a), len(b)

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result
