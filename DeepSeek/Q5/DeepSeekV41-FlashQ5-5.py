def remove_duplicates(numbers):
    """Return a new list with duplicates removed, keeping first occurrences.

    The original order is preserved and the input list is not modified.
    """
    seen = set()
    result = []
    for value in numbers:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
