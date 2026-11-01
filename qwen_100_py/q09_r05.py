def rotate_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    n = len(matrix)
    return [
        [matrix[row][col] for row in range(n - 1, -1, -1)]
        for col in range(n)
    ]
