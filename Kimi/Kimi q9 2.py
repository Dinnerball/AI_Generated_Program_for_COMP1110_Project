def rotate_matrix(matrix):
    if not matrix:
        return []
    return [[row[i] for row in reversed(matrix)] for i in range(len(matrix))]
