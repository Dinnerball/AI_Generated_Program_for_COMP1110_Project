"""Q10: return the longest contiguous strictly increasing run of a list.

The existing ``longest_increasing_run.py`` in this folder was left untouched;
this module is an additional copy of the same solution.
"""


def longest_increasing_run(numbers):
    """Return the longest contiguous strictly increasing sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A new list holding the longest run of values that are consecutive
        positions in ``numbers`` and strictly increasing. Ties are broken by
        taking the earliest run. An empty input returns an empty list.

    The input list is not modified and nothing is printed.
    """
    best_start = 0
    best_length = 0

    start = 0
    for index in range(1, len(numbers) + 1):
        # index == len(numbers) closes the final run.
        if index == len(numbers) or numbers[index] <= numbers[index - 1]:
            length = index - start
            # Strict ">" keeps the earlier run when lengths are equal.
            if length > best_length:
                best_start = start
                best_length = length
            start = index

    return list(numbers[best_start:best_start + best_length])


if __name__ == "__main__":
    raise SystemExit("Import longest_increasing_run from this module instead.")
