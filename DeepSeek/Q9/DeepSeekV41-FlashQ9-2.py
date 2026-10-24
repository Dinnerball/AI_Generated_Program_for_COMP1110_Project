"""Rotate an n x n integer matrix 90 degrees clockwise."""


def rotate_matrix(matrix):
    """Return a new matrix rotated 90 degrees clockwise.

    Args:
        matrix: an n x n square matrix as a list of lists of integers.
            An empty matrix is allowed and returns an empty list.

    Returns:
        A new list of lists holding the input rotated 90 degrees clockwise.
        The original matrix is not modified and nothing is printed.

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
        # Empty matrix wraps around to an empty matrix.
        return []

    # A clockwise turn sends the element at (row r, col c) to (col c, row n-1-r),
    # so the element now at row r, col c came from row n-1-c, col r.
    return [[matrix[n - 1 - c][r] for c in range(n)] for r in range(n)]
