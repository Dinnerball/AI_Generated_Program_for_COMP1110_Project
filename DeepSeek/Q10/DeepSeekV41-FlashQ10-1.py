"""Q10: longest contiguous strictly increasing run in a list of integers."""


def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing run of ``numbers``.

    Elements in the returned list keep their original positions and are
    consecutive in the input. When several runs tie for the maximum length,
    the one that appears first is returned. An empty input yields an empty
    list. The input list is never modified and nothing is printed.
    """
    best_start = 0
    best_length = 0

    start = 0
    for index in range(1, len(numbers) + 1):
        # ``index == len(numbers)`` closes the final run.
        if index == len(numbers) or numbers[index] <= numbers[index - 1]:
            length = index - start
            # Strict ">" keeps the earlier run when lengths are equal.
            if length > best_length:
                best_start = start
                best_length = length
            start = index

    return list(numbers[best_start:best_start + best_length])
