def rotate_matrix(matrix):
    """
    Rotate an n x n matrix 90 degrees clockwise.

    Args:
        matrix: A list of lists of integers (square matrix).

    Returns:
        A new matrix rotated 90 degrees clockwise, without
        modifying the original. Empty input returns [].
    """
    if not matrix:
        return []
    return [list(col) for col in zip(*matrix[::-1])]
