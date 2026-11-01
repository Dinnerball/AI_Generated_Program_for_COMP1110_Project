def rotate_matrix(matrix):
    if not matrix:
        return []

    n = len(matrix)
    rotated = []

    for col in range(n):
        rotated.append([matrix[row][col] for row in range(n - 1, -1, -1)])

    return rotated
