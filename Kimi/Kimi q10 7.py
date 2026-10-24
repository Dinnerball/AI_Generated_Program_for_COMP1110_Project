def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing run in numbers.

    If several runs share the maximum length, the earliest one is returned.
    The input list is not modified.
    """
    if not numbers:
        return []

    best_start = 0
    best_len = 1
    cur_start = 0
    cur_len = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            cur_len += 1
            if cur_len > best_len:
                best_len = cur_len
                best_start = cur_start
        else:
            cur_start = i
            cur_len = 1

    return list(numbers[best_start:best_start + best_len])
