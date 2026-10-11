def rotate_matrix(matrix):
    """
    Rotate an n x n square matrix 90 degrees clockwise.

    Args:
        matrix: list of lists of integers, the square matrix to rotate.

    Returns:
        A new matrix rotated 90 degrees clockwise.
        Returns an empty list if the input is empty.
        The original matrix is not modified.
    """
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix[::-1])]
