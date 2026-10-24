"""Q10: longest contiguous strictly increasing run in a list of integers.

This is a newly added module. The Python files that were already present in
this folder (``longest_increasing_run.py``, ``longest_increasing_run_q10.py``,
``longest_increasing_run_solution.py`` and ``test_longest_increasing_run.py``)
were left untouched.
"""


def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing run of ``numbers``.

    The result is a new list whose values appear in the same order and at
    consecutive positions in ``numbers``, and each value is strictly greater
    than the one before it. If two or more runs tie for the greatest length,
    the one appearing earliest in the input is returned. An empty input gives
    an empty list.

    The input list is never modified and nothing is printed.

    Args:
        numbers: A list of integers.

    Returns:
        A new list containing the longest contiguous strictly increasing run.
    """
    best_start = 0
    best_length = 0

    start = 0
    # ``len(numbers)`` acts as a sentinel that closes the run at the end.
    for index in range(1, len(numbers) + 1):
        if index == len(numbers) or numbers[index] <= numbers[index - 1]:
            length = index - start
            # Strict ">" keeps the earlier run when two runs tie in length.
            if length > best_length:
                best_start = start
                best_length = length
            start = index

    return list(numbers[best_start:best_start + best_length])


if __name__ == "__main__":
    print(longest_increasing_run([1, 2, 3, 2, 4, 5, 6, 1]))  # [2, 4, 5, 6]
    print(longest_increasing_run([1, 2, 9, 3, 4]))            # [1, 2, 9]
    print(longest_increasing_run([]))                          # []
