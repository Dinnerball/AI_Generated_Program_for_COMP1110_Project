"""Q10: longest contiguous strictly increasing run in a list of integers.

This is a NEW file. Every Python file that already existed in this directory
(longest_increasing_run.py, longest_increasing_run_q10.py,
longest_increasing_run_solution.py, longest_increasing_run_v2.py,
longest_increasing_run_final.py, q10_longest_increasing_run.py and
test_longest_increasing_run.py) was left completely untouched.
"""


def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing sequence of values.

    The returned values occupy consecutive positions in the original list.
    If several runs share the maximum length, the earliest one is returned.
    An empty input yields ``[]``. The input list is never modified and
    nothing is printed.

    Args:
        numbers: A list of integers (any sequence supporting len/indexing).

    Returns:
        A new list holding the longest strictly increasing contiguous run,
        or ``[]`` when ``numbers`` is empty.
    """
    # Work on the sequence as given: only reads, never writes.
    n = len(numbers)
    if n == 0:
        return []

    best_start = 0
    best_len = 1
    run_start = 0

    for i in range(1, n):
        if numbers[i] > numbers[i - 1]:
            # The current increasing run simply extends.
            continue
        # The run that ended at i - 1 is [run_start, i).
        run_len = i - run_start
        if run_len > best_len:  # '>' keeps the earliest run on ties.
            best_len = run_len
            best_start = run_start
        run_start = i

    # Close the final run, which ends at n - 1.
    run_len = n - run_start
    if run_len > best_len:
        best_len = run_len
        best_start = run_start

    return list(numbers[best_start:best_start + best_len])
