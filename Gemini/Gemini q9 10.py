def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Returns a new n x n matrix rotated 90 degrees clockwise."""
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    
    for r in range(n):
        for c in range(n):
            rotated[c][n - 1 - r] = matrix[r][c]
            
    return rotated

