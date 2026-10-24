"""COMP1110 Q10 - longest contiguous strictly increasing run."""


def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing subsequence.

    Elements must occupy consecutive positions in `numbers`. If several
    runs share the maximum length, the earliest one is returned. An empty
    input yields an empty list. The input list is never modified.
    """
    if not numbers:
        return []

    best_start = 0
    best_length = 1
    run_start = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            # Run continues; its length is i - run_start + 1.
            if i - run_start + 1 > best_length:
                best_start = run_start
                best_length = i - run_start + 1
        else:
            # Run breaks here; a new run starts at the current element.
            run_start = i

    return numbers[best_start:best_start + best_length]
