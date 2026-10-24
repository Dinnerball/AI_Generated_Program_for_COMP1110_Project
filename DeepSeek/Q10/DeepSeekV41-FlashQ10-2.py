"""Q10 - longest contiguous strictly increasing run.

This module adds a NEW file (longest_increasing_run_final.py) and does not
modify or overwrite any pre-existing file in the directory.
"""


def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing sequence of numbers.

    Elements must occupy consecutive positions in the original list.
    Ties are broken by earliest occurrence. An empty input yields [].

    The input list is never modified and nothing is printed.

    Args:
        numbers: an iterable of integers (a list is expected).

    Returns:
        A new list holding the first longest strictly increasing run.
    """
    values = list(numbers)

    if not values:
        return []

    best_start = 0
    best_length = 1
    run_start = 0

    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            # Strictly increasing: the current run simply grows.
            current_length = i - run_start + 1
            if current_length > best_length:
                best_length = current_length
                best_start = run_start
        else:
            # Strict increase broken here, so a new run starts at i.
            run_start = i

    return values[best_start:best_start + best_length]


if __name__ == "__main__":
    # Minimal self-check (no printing of results required by the spec;
    # this block only runs when the file is executed directly).
    assert longest_increasing_run([]) == []
    assert longest_increasing_run([5]) == [5]
    assert longest_increasing_run([1, 2, 3, 0, 4, 5, 6]) == [0, 4, 5, 6]
    assert longest_increasing_run([3, 2, 1]) == [3]
    assert longest_increasing_run([1, 5, 2, 6, 3, 7]) == [1, 5]
    assert longest_increasing_run([-3, -2, -1, 0]) == [-3, -2, -1, 0]
