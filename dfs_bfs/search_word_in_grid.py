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

