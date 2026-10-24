def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merges two sorted lists into one new sorted list."""
    result = []
    i, j = 0, 0
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
            
    result.extend(a[i:])
    result.extend(b[j:])
    return result

