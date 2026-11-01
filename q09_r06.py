def rotate_matrix(matrix):
    """
    Return a new n x n matrix rotated 90 degrees clockwise.
    """
    if not matrix or not matrix[0]:
        return []

    n = len(matrix)
    return [[matrix[n - 1 - col][row] for col in range(n)] for row in range(n)]
