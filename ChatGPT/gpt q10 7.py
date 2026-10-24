def longest_increasing_run(numbers):
    if not numbers:
        return []

    best_start = 0
    best_length = 1
    current_start = 0
    current_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_length += 1
        else:
            if current_length > best_length:
                best_start = current_start
                best_length = current_length
            current_start = i
            current_length = 1

    # Check the final run
    if current_length > best_length:
        best_start = current_start
        best_length = current_length

    return numbers[best_start:best_start + best_length]