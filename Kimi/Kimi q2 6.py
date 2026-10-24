def second_largest(numbers):
    first = second = None
    for n in numbers:
        if first is None or n > first:
            if n != first:
                second = first
            first = n
        elif n != first and (second is None or n > second):
            second = n
    return second