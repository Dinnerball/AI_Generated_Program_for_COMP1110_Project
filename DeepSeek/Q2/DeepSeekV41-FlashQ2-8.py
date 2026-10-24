def second_largest(numbers):
    """Return the second largest distinct value in `numbers`.

    Returns None when the sequence contains fewer than two distinct values.
    The input list is not modified and nothing is printed.
    """
    largest = None
    second = None

    for value in numbers:
        if largest is None or value > largest:
            second = largest
            largest = value
        elif value < largest and (second is None or value > second):
            second = value

    return second
