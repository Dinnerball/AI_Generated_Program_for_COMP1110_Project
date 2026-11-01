def rotate_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    n = len(matrix)
    return [[matrix[n - 1 - r][c] for r in range(n)] for c in range(n)]
