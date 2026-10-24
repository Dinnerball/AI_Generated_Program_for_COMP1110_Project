def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Returns a new matrix rotated 90 degrees clockwise."""
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]
    
    for r in range(n):
        for c in range(n):
            new_matrix[c][n - 1 - r] = matrix[r][c]
            
    return new_matrix

