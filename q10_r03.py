def longest_increasing_run(numbers):
    """
    Returns the longest contiguous strictly increasing subsequence of values
    in a list of integers. If there is a tie, returns the first occurrence.
    Returns an empty list if the input list is empty.
    """
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
            current_start = i
            current_length = 1

        if current_length > best_length:
            best_start = current_start
            best_length = current_length

    return numbers[best_start:best_start + best_length]
