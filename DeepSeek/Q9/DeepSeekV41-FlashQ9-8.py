"""Q9: rotate an n x n integer matrix 90 degrees clockwise."""


def rotate_matrix(matrix):
    """Return a new n x n matrix rotated 90 degrees clockwise.

    Args:
        matrix: An n x n square matrix given as a list of lists of integers.
            An empty matrix is allowed and returns an empty list.

    Returns:
        A new list of lists holding the input rotated 90 degrees clockwise.
        The original matrix is left unmodified and nothing is printed.
        For an empty input the result is an empty list.

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

    # Element (r, c) moves to (c, n - 1 - r); inverting that mapping means the
    # value now at (r, c) came from (n - 1 - c, r). Building a fresh list of
    # lists keeps the caller's matrix untouched.
    return [[matrix[n - 1 - c][r] for c in range(n)] for r in range(n)]


if __name__ == "__main__":
    # Self-check that runs only when this file is executed directly.
    assert rotate_matrix([]) == []
    assert rotate_matrix([[1]]) == [[1]]
    assert rotate_matrix([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    assert rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    assert rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]

    # The original matrix must survive the call unchanged.
    original = [[1, 2], [3, 4]]
    result = rotate_matrix(original)
    assert original == [[1, 2], [3, 4]]
    assert result is not original

    print("All checks passed.")
