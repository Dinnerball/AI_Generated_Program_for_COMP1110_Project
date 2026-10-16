def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing run in ``numbers``.

    The run consists of elements at consecutive positions of the original
    list, and each element must be strictly greater than the one before it.
    When several runs share the maximum length, the earliest one is returned.
    An empty list yields an empty list.  The input list is never modified and
    nothing is printed.

    >>> longest_increasing_run([1, 2, 3, 2, 4, 5])
    [1, 2, 3]
    >>> longest_increasing_run([3, 2, 1])
    [3]
    >>> longest_increasing_run([])
    []
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

        # Strict ">" keeps the first run when lengths tie.
        if current_length > best_length:
            best_length = current_length
            best_start = current_start

    return list(numbers[best_start:best_start + best_length])
