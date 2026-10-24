def rotate_matrix(matrix):
    if not matrix:
        return []

    n = len(matrix)
    return [[matrix[n - 1 - row][col] for row in range(n)] for col in range(n)]