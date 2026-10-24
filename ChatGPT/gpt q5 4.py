def remove_duplicates(numbers):
    result = []
    seen = set()

    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result