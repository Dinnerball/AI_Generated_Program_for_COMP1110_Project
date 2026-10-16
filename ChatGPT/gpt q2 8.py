def second_largest(numbers):
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers)[-2]