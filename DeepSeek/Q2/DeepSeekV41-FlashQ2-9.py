"""COMP1110 Q2: return the second largest distinct value in a list of integers."""


def second_largest(numbers):
    """Return the second largest distinct integer in ``numbers``.

    Returns ``None`` when the list contains fewer than two distinct values.
    The original list is never modified and nothing is printed.
    """
    largest = None
    second = None

    for value in numbers:
        if largest is None or value > largest:
            second = largest
            largest = value
        elif value != largest and (second is None or value > second):
            second = value

    return second
