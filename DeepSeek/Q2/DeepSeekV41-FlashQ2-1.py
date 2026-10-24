def second_largest(numbers):
    """Return the second largest distinct number in a list of integers.

    Returns None if the list contains fewer than two distinct values.
    The original list is not modified and nothing is printed.
    """
    distinct = set(numbers)
    if len(distinct) < 2:
        return None

    largest = max(distinct)
    return max(value for value in distinct if value != largest)
