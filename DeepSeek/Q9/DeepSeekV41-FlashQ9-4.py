"""Q9: rotate an n x n matrix 90 degrees clockwise."""


def rotate_matrix(matrix):
    """Return a new matrix rotated 90 degrees clockwise.

    The input is an n x n square matrix given as a list of lists of integers.
    An empty matrix returns an empty list. Neither the input matrix nor any of
    its rows is modified, and nothing is printed.
    """
    if not matrix:
        return []

    n = len(matrix)
    return [[matrix[n - 1 - row][col] for row in range(n)] for col in range(n)]
