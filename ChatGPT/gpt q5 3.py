def remove_duplicates(numbers):
    result = []
    seen = set()

    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result