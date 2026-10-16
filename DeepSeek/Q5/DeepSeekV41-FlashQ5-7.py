def remove_duplicates(numbers):
    """Return a new list with duplicate values removed.

    Only the first occurrence of each value is kept, the original order is
    preserved, and the input list is never modified.
    """
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result
