def rotate_matrix(matrix: list) -> list:
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            new_matrix[col][n - 1 - row] = matrix[row][col]
            
    return new_matrix

