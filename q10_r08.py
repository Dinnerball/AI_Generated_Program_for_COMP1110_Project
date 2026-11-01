def longest_increasing_run(numbers):
    """
    Return the longest contiguous strictly increasing subsequence from numbers.

    If multiple runs have the same maximum length, returns the first one.
    If numbers is empty, returns an empty list.
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
            if current_length > best_length:
                best_length = current_length
                best_start = current_start

            current_start = i
            current_length = 1

    if current_length > best_length:
        best_length = current_length
        best_start = current_start

    return list(numbers[best_start:best_start + best_length])
