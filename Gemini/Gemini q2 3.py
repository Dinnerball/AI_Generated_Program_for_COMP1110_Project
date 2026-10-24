def second_largest(numbers: list[int]):
    distinct_nums = list(set(numbers))
    if len(distinct_nums) < 2:
        return None
    distinct_nums.sort(reverse=True)
    return distinct_nums[1]

