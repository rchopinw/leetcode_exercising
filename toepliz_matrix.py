# LC 766 Toeplitz Matrix
def toep_matrix(matrix):
    ny, nx = len(matrix), len(matrix[0])
    if ny <= 1 or nx <= 1:
        return True
    # check column
    for x in range(nx):
        y = 0
        prev = matrix[y][x]
        new_x, new_y = x, y
        while 0 <= new_x < nx and 0 <= new_y < ny:
            if prev != matrix[new_y][new_x]:
                return False
            prev = matrix[new_y][new_x]
            new_x += 1
            new_y += 1
    # check row:
    for y in range(1, ny):
        x = 0
        prev = matrix[y][x]
        new_x, new_y = x, y
        while 0 <= new_x < nx and 0 <= new_y < ny:
            if prev != matrix[new_y][new_x]:
                return False
            prev = matrix[new_y][new_x]
            new_x += 1
            new_y += 1
    return True