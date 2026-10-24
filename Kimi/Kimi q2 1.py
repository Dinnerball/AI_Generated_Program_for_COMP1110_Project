def second_largest(numbers):
    largest = second = None
    for n in numbers:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif n != largest and (second is None or n > second):
            second = n
    return second