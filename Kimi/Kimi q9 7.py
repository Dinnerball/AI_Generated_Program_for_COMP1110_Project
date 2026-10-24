def rotate_matrix(matrix):
    if not matrix:
        return []
    return [list(col) for col in zip(*matrix[::-1])]
