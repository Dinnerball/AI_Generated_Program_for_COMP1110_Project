"""COMP1110 group project - Q2.

second_largest(numbers) returns the second largest *distinct* value in a list
of integers, or None when the list contains fewer than two distinct values.

The input list is never modified and nothing is printed.
"""


def second_largest(numbers):
    """Return the second largest distinct integer in ``numbers``.

    Args:
        numbers: an iterable/list of integers.

    Returns:
        The second largest distinct value, or ``None`` if there are fewer
        than two distinct values.

    Examples:
        >>> second_largest([1, 5, 3])
        3
        >>> second_largest([4, 4, 4])
        >>> second_largest([])
    """
    # A set build copies the values, so the original list stays untouched.
    distinct = set(numbers)

    if len(distinct) < 2:
        return None

    distinct.remove(max(distinct))
    return max(distinct)
