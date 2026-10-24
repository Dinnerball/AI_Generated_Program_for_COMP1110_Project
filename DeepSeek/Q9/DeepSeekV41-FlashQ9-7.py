"""Rotate an n x n matrix 90 degrees clockwise (non-destructive)."""


def rotate_matrix(matrix):
    """Return a new matrix rotated 90 degrees clockwise.

    Args:
        matrix: A square matrix as a list of lists of integers.
            An empty matrix yields an empty list.

    Returns:
        A new list of lists; the input matrix is never modified.
    """
    n = len(matrix)
    if n == 0:
        return []

    # Row i of the result is column i of the input read bottom-to-top.
    return [[matrix[n - 1 - row][col] for row in range(n)] for col in range(n)]
