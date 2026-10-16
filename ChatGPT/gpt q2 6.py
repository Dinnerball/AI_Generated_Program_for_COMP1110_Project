def second_largest(numbers):
    distinct = sorted(set(numbers), reverse=True)
    return distinct[1] if len(distinct) >= 2 else None