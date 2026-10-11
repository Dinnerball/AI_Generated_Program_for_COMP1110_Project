def rotate_matrix(matrix):
    if not matrix:
        return []
    return [[matrix[i][j] for i in range(len(matrix) - 1, -1, -1)]
            for j in range(len(matrix))]
