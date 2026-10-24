def second_largest(numbers):
    distinct_nums = set(numbers)
    if len(distinct_nums) < 2:
        return None
    return sorted(distinct_nums)[-2]

