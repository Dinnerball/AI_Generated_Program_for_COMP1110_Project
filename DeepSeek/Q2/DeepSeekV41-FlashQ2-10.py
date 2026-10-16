def second_largest(numbers):
    """Return the second largest distinct number in a list of integers.

    Returns None if there are fewer than two distinct values.
    The original list is not modified and nothing is printed.
    """
    # Iterate without mutating: we only track the top two distinct values.
    largest = None
    second = None

    for value in numbers:
        if largest is None or value > largest:
            # New maximum: the old maximum becomes the runner-up.
            if largest is not None and largest != value:
                second = largest
            largest = value
        elif value != largest:
            # value < largest here; it may still beat the current runner-up.
            if second is None or value > second:
                second = value

    return second
