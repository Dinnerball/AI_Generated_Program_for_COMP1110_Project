def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix or not matrix[0]:
        return []
    
    # 逆序行然后用 zip 解包，生成全新矩阵，不修改原矩阵
    return [list(row) for row in zip(*matrix[::-1])]

