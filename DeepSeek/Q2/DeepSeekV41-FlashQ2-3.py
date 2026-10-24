def second_largest(numbers):
    """Return the second largest distinct number in a list of integers.

    Returns None if there are fewer than two distinct values.
    The original list is not modified and nothing is printed.
    """
    # sorted() builds a new list, so the caller's list is left untouched.
    distinct = sorted(set(numbers), reverse=True)
    if len(distinct) < 2:
        return None
    return distinct[1]
