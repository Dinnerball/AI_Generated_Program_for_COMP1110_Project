def rotate_matrix(matrix):
    """Return a new matrix rotated 90 degrees clockwise.

    matrix is an n x n square matrix (list of lists) of integers.
    The original matrix is not modified. An empty matrix returns [].
    """
    n = len(matrix)
    if n == 0:
        return []

    # New row i comes from column i of the original, read bottom-to-top.
    return [[matrix[n - 1 - row][col] for row in range(n)] for col in range(n)]
