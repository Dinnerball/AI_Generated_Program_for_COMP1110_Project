"""Q9: rotate an n x n matrix 90 degrees clockwise."""


def rotate_matrix(matrix):
    """Return a new matrix rotated 90 degrees clockwise.

    Args:
        matrix: an n x n square matrix given as a list of lists of integers.
            An empty matrix is allowed and yields an empty list.

    Returns:
        A new list of lists representing the input rotated 90 degrees
        clockwise. The original matrix is left untouched and nothing is
        printed.

    Examples:
        >>> rotate_matrix([])
        []
        >>> rotate_matrix([[1, 2], [3, 4]])
        [[3, 1], [4, 2]]
        >>> rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    n = len(matrix)
    if n == 0:
        return []

    # The element at row r, column c moves to row c, column (n - 1 - r).
    return [[matrix[n - 1 - c][r] for c in range(n)] for r in range(n)]


if __name__ == "__main__":
    # Lightweight self-check; only runs when this file is executed directly.
    assert rotate_matrix([]) == []
    assert rotate_matrix([[1]]) == [[1]]
    assert rotate_matrix([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    assert rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    original = [[1, 2], [3, 4]]
    rotate_matrix(original)
    assert original == [[1, 2], [3, 4]]
    print("All checks passed.")
