"""COMP1110 Q9 - rotate an n x n matrix 90 degrees clockwise."""


def rotate_matrix(matrix):
    """Return a new matrix rotated 90 degrees clockwise.

    Args:
        matrix: an n x n square matrix as a list of lists of integers.

    Returns:
        A new list of lists. The original matrix is not modified.
        An empty matrix returns an empty list.
    """
    n = len(matrix)
    if n == 0:
        return []

    # result[i][j] = matrix[n - 1 - j][i]
    return [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    assert rotate_matrix([]) == []
    assert rotate_matrix([[1]]) == [[1]]
    assert rotate_matrix([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    assert rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    original = [[1, 2], [3, 4]]
    rotated = rotate_matrix(original)
    assert original == [[1, 2], [3, 4]], "original matrix was modified"
    assert rotated is not original
