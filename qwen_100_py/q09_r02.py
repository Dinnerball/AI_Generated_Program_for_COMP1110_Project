def rotate_matrix(matrix):
    """
    Returns a new n x n matrix rotated 90 degrees clockwise.

    Args:
        matrix: A square list of lists containing integers.

    Returns:
        A new rotated matrix. If the input is empty, returns an empty list.
    """
    if not matrix:
        return []

    n = len(matrix)

    return [
        [matrix[n - 1 - row][col] for row in range(n)]
        for col in range(n)
    ]
