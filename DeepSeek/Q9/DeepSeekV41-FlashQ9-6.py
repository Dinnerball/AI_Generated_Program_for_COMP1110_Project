"""Q9: Rotate an n x n integer matrix 90 degrees clockwise.

Returns a brand-new matrix; the input matrix is never modified and
nothing is printed.
"""


def rotate_matrix(matrix):
    """Return a new matrix that is `matrix` rotated 90 degrees clockwise.

    Args:
        matrix: an n x n square matrix given as a list of lists of ints.

    Returns:
        A new list of lists of ints. An empty matrix returns an empty list.
    """
    if not matrix:
        return []

    n = len(matrix)
    # The element at row r, column c moves to row c, column n - 1 - r.
    return [[matrix[n - 1 - c][r] for c in range(n)] for r in range(n)]
