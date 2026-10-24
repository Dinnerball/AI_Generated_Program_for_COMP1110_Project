def rotate_matrix(matrix):
    if not matrix:
        return []
    # zip(*reversed(matrix)) reverses the rows, then transposes,
    # which is equivalent to a 90° clockwise rotation.
    return [list(row) for row in zip(*reversed(matrix))]
