def remove_duplicates(numbers):
    """Return a new list containing each value of numbers once.

    Only the first occurrence of each value is kept, the original order is
    preserved, and the input list is left unmodified. Nothing is printed.
    """
    seen = set()
    result = []
    for value in numbers:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


if __name__ == "__main__":
    # Simple self-checks: run "python q5_remove_duplicates_first_occurrence.py"
    original = [1, 2, 1, 3, 2, 4, 4, 4]
    snapshot = original[:]
    assert remove_duplicates(original) == [1, 2, 3, 4]
    assert original == snapshot, "input list must not be modified"
    assert remove_duplicates([]) == []
    assert remove_duplicates([7, 7, 7]) == [7]
    assert remove_duplicates([-1, 0, -1, 0]) == [-1, 0]
