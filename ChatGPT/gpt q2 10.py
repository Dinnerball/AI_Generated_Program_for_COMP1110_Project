def second_largest(numbers):
    distinct = set(numbers)
    if len(distinct) < 2:
        return None
    return sorted(distinct, reverse=True)[1]