# LC 79 Word Search
def word_search(grid, word):
    ny, nx = len(grid), len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(y, x, idx):
        if idx == len(word):
            return True

        if not (0 <= y < ny and 0 <= x < nx) or word[idx] != grid[y][x]:
            return False

        flag = False
        grid[y][x] = "#"
        for dx, dy in directions:
            flag = dfs(y + dy, x + dx, idx + 1)
            if flag:
                break
        grid[y][x] = word[idx]
        return flag

    for y in range(ny):
        for x in range(nx):
            if grid[y][x] == word[0] and dfs(y, x, 0):
                return True

    return False


def search_word_in_grid_ii(board, word):
    ny, nx = len(board), len(board[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(y, x, idx):
        if idx == len(word) - 1:
            return True

        flag = False
        board[y][x] = '!'
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < nx and 0 <= new_y < ny and board[new_y][new_x] == word[idx + 1]:
                flag = dfs(new_y, new_x, idx + 1)
                if flag:
                    break
        board[y][x] = word[idx]
        return flag

    for y in range(ny):
        for x in range(nx):
            if board[y][x] == word[0] and dfs(y, x, 0):
                return True
    return False


