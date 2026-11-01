def longest_increasing_run(numbers):
    """
    Return the longest contiguous strictly increasing subsequence of values.

    If multiple runs have the same maximum length, return the first one.
    If the input list is empty, return an empty list.
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
            best_length = current_length
            best_start = current_start

    return numbers[best_start:best_start + best_length]
