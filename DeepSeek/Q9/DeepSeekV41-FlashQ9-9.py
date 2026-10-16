"""Rotate an n x n matrix 90 degrees clockwise (non-destructive)."""


def rotate_matrix(matrix):
    """Return a new matrix rotated 90 degrees clockwise.

    Args:
        matrix: An n x n square matrix as a list of lists of integers.
            An empty matrix returns an empty list.

    Returns:
        A brand-new list of lists. The original matrix is left untouched,
        and nothing is printed.
    """
    n = len(matrix)
    if n == 0:
        return []

    # The first row of the result is the last column of the input read
    # top-to-bottom, so result[row][col] == matrix[n - 1 - col][row].
    return [[matrix[n - 1 - col][row] for col in range(n)] for row in range(n)]
