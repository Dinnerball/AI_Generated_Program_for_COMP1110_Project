def second_largest(numbers: list[int]):
    """Returns the second largest distinct number in a list, or None."""
    distinct_numbers = list(set(numbers))
    if len(distinct_numbers) < 2:
        return None
    distinct_numbers.sort(reverse=True)
    return distinct_numbers[1]

