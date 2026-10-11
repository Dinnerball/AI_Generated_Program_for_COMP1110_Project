def second_largest(numbers):
    distinct = set(numbers)
    if len(distinct) < 2:
        return None
    distinct.remove(max(distinct))
    return max(distinct)