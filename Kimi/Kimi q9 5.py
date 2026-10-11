def rotate_matrix(matrix):
    """
    Rotate an n x n matrix 90 degrees clockwise.

    Args:
        matrix: A list of lists of integers representing an n x n matrix.

    Returns:
        A new list of lists representing the rotated matrix.
        Returns an empty list if the input is empty.
    """
    if not matrix:
        return []
    return [list(col) for col in zip(*matrix[::-1])]
