def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing subsequence.

    In case of a tie, the first occurring run is returned.
    The input list is not modified.
    """
    if not numbers:
        return []

    best_start, best_len = 0, 1
    run_start = 0

    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            run_start = i
        run_len = i - run_start + 1
        if run_len > best_len:
            best_start, best_len = run_start, run_len

    return numbers[best_start:best_start + best_len]
