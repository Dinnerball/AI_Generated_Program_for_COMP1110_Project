def remove_duplicates(numbers: list[int]) -> list[int]:
    """Returns a new list with duplicate values removed, keeping the first occurrence."""
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

