def rotate_matrix(matrix):
    """
    Return a new n x n matrix rotated 90 degrees clockwise.
    """
    if not matrix:
        return []

    return [list(row) for row in zip(*matrix[::-1])]
