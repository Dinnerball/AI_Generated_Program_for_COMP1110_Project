def remove_duplicates(numbers):
    """Return a new list with duplicates removed, keeping first occurrences.

    The original order is preserved and the input list is left unchanged.
    """
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result
