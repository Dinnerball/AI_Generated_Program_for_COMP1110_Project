def longest_increasing_run(numbers):
    if not numbers:
        return []

    best_start = start = 0
    best_len = length = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            length += 1
        else:
            start = i
            length = 1
        if length > best_len:
            best_len = length
            best_start = start

    return numbers[best_start:best_start + best_len]
