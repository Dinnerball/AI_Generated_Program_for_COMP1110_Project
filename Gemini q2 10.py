def second_largest(numbers: list[int]):
    """Returns the second largest distinct number, or None if fewer than two exist."""
    distinct_nums = set(numbers)
    if len(distinct_nums) < 2:
        return None
    return sorted(distinct_nums)[-2]

