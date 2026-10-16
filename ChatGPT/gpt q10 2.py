def longest_increasing_run(numbers):
    if not numbers:
        return []

    longest_start = 0
    longest_length = 1

    current_start = 0
    current_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_length += 1
        else:
            if current_length > longest_length:
                longest_start = current_start
                longest_length = current_length
            current_start = i
            current_length = 1

    # Check the final run
    if current_length > longest_length:
        longest_start = current_start
        longest_length = current_length

    return numbers[longest_start:longest_start + longest_length]