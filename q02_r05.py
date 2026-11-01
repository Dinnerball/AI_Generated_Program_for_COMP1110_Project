def second_largest(numbers):
    largest = None
    second = None

    for n in numbers:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif n < largest:
            if second is None or n > second:
                second = n

    return second
