"""Q10: longest contiguous strictly increasing run in a list of integers.

This is a NEW file. Every Python file that already existed in this directory
(longest_increasing_run.py, longest_increasing_run_q10.py,
longest_increasing_run_solution.py, longest_increasing_run_v2.py,
longest_increasing_run_final.py and test_longest_increasing_run.py) was left
completely untouched.
"""


def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing run of ``numbers``.

    The returned list holds values taken from consecutive positions of the
    original list, in their original order, where every value is strictly
    greater than the value before it. If two or more runs tie for the greatest
    length, the one that occurs first in the input is returned. An empty input
    yields an empty list.

    The input list is never modified and nothing is printed.

    Args:
        numbers: A list of integers.

    Returns:
        A new list containing the first longest strictly increasing run.
    """
    best_start = 0
    best_length = 0

    run_start = 0
    # ``len(numbers)`` is used as a sentinel that closes the final run, so the
    # loop body never has to special-case the end of the list.
    for index in range(1, len(numbers) + 1):
        # A run ends when we pass the last element or the increase is broken
        # (<= keeps duplicates and decreases out of the run).
        if index == len(numbers) or numbers[index] <= numbers[index - 1]:
            length = index - run_start
            # Strict ">" means an equally long later run never replaces the
            # earlier one, which gives the required first-occurrence tie-break.
            if length > best_length:
                best_start = run_start
                best_length = length
            run_start = index

    return list(numbers[best_start:best_start + best_length])


if __name__ == "__main__":
    # Self-check only; the function itself never prints anything.
    assert longest_increasing_run([]) == []
    assert longest_increasing_run([7]) == [7]
    assert longest_increasing_run([1, 2, 3, 2, 4, 5, 6, 1]) == [2, 4, 5, 6]
    assert longest_increasing_run([1, 2, 9, 3, 4]) == [1, 2, 9]
    assert longest_increasing_run([3, 2, 1]) == [3]
    assert longest_increasing_run([5, 5, 5]) == [5]
    assert longest_increasing_run([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert longest_increasing_run([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert longest_increasing_run([2, 2, 3, 4]) == [2, 3, 4]
    assert longest_increasing_run([-3, -2, -1, 0]) == [-3, -2, -1, 0]
    assert longest_increasing_run([0, -1, -2]) == [0]
