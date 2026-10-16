"""Return the second largest distinct value of a list of integers."""


def second_largest(numbers):
    """Return the second largest distinct number in ``numbers``.

    Returns ``None`` when the list has fewer than two distinct values.
    The original list is not modified and nothing is printed.
    """
    largest = None
    second = None
    for value in numbers:
        if largest is None or value > largest:
            second = largest      # the old maximum becomes the runner-up
            largest = value
        elif value < largest and (second is None or value > second):
            second = value
    return second


if __name__ == "__main__":
    assert second_largest([3, 1, 4, 1, 5, 9, 2, 6]) == 6
    assert second_largest([10, 10, 7, 7, 3]) == 7
    assert second_largest([5, 5, 5]) is None
    assert second_largest([]) is None
    assert second_largest([4]) is None
    assert second_largest([-1, -7, -3]) == -3
    data = [2, 2, 9, 1]
    second_largest(data)
    assert data == [2, 2, 9, 1]
    print("all tests passed")
