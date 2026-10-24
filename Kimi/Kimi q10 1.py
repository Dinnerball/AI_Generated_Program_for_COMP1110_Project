def longest_increasing_run(numbers):
    """
    Return the longest contiguous strictly increasing sequence in numbers.
    Ties are broken by earliest occurrence. Empty input returns [].
    """
    if not numbers:
        return []

    best_start = start = 0
    best_len = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            if i - start + 1 > best_len:
                best_start = start
                best_len = i - start + 1
        else:
            start = i

    return numbers[best_start:best_start + best_len]
