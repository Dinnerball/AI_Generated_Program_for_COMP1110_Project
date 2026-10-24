def remove_duplicates(numbers):
    """Return a new list with duplicate values removed.

    Only the first occurrence of each value is kept, the original order is
    preserved, and the input list is not modified. Nothing is printed.
    """
    seen = set()
    result = []
    for value in numbers:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
