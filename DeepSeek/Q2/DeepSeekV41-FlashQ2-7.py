def second_largest(numbers):
    """Return the second largest distinct number in ``numbers``.

    The input list is not modified. If there are fewer than two distinct
    values, ``None`` is returned.
    """
    largest = None
    runner_up = None

    for value in numbers:
        if largest is None or value > largest:
            runner_up = largest
            largest = value
        elif value != largest and (runner_up is None or value > runner_up):
            runner_up = value

    return runner_up


if __name__ == "__main__":
    assert second_largest([1, 2, 3, 4]) == 3
    assert second_largest([5, 5, 5]) is None
    assert second_largest([7]) is None
    assert second_largest([]) is None
    assert second_largest([-1, -5, -3]) == -3
    data = [4, 4, 2, 9, 9, 6]
    assert second_largest(data) == 6
    assert data == [4, 4, 2, 9, 9, 6]
