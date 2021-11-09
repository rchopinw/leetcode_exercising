# LC 1428 Leftmost column with at least a one
class BinaryMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, row, col):
        return self.matrix[row][col]

    def dimension(self):
        return len(self.matrix), len(self.matrix[0])


def left_most_column_with_one(bm: BinaryMatrix):
    ny, nx = bm.dimension()
    y, x = 0, nx - 1
    flag = False
    while True:
        if bm.get(y, x) == 1:
            flag = True
            x -= 1
        else:
            y += 1
        if y == ny or x == -1:
            return x + 1 if flag else -1