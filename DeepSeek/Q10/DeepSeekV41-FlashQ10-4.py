"""Q10: longest contiguous strictly increasing run in a list of integers.

This module is a new file; the pre-existing ``longest_increasing_run.py`` and
``longest_increasing_run_q10.py`` in this folder were left untouched.
"""


def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing run of ``numbers``.

    The returned values keep their original order and come from consecutive
    positions in ``numbers``. If several runs share the maximum length, the
    one appearing first is returned. An empty input gives an empty list.

    The input list is never modified and nothing is printed.
    """
    best_start = 0
    best_length = 0

    start = 0
    for index in range(1, len(numbers) + 1):
        # Treat index == len(numbers) as the end marker that closes the last run.
        if index == len(numbers) or numbers[index] <= numbers[index - 1]:
            length = index - start
            # Strict ">" keeps the earlier run when two runs tie in length.
            if length > best_length:
                best_start = start
                best_length = length
            start = index

    return list(numbers[best_start:best_start + best_length])


if __name__ == "__main__":
    print(longest_increasing_run([1, 2, 3, 2, 4, 5, 6, 1]))
    print(longest_increasing_run([]))
    print(longest_increasing_run([5, 5, 5]))
