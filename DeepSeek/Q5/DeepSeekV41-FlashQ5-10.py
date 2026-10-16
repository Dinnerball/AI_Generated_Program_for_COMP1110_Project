def remove_duplicates(numbers):
    """Return a new list containing the first occurrence of each value.

    Duplicate values are dropped, the original order is preserved, and the
    input list is never modified. Nothing is printed.
    """
    seen = set()
    result = []
    for value in numbers:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
