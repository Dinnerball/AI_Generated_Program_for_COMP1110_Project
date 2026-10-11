def second_largest(numbers):
    """Return the second largest distinct number, or None if fewer than two distinct values."""
    largest = second = None
    for n in numbers:
        if largest is None or n > largest:
            largest, second = n, largest
        elif n != largest and (second is None or n > second):
            second = n
    return second