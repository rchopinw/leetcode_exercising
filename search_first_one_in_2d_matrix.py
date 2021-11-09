# LC 240: Search a 2D matrix
def search_2d_matrix(matrix, target):
    y, x = 0, len(matrix[0]) - 1
    while y < len(matrix) and x >= 0:
        if matrix[y][x] == target:
            return True
        elif matrix[y][x] < target:
            y += 1
        else:
            x -= 1
    return False
