def rotate_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    return [list(row) for row in zip(*matrix[::-1])]
