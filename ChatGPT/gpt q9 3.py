def rotate_matrix(matrix):
    if not matrix:
        return []

    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
