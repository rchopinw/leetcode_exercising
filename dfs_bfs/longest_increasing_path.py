# LC 329: Longest increasing path
def longest_increasing_path(matrix):
    ny, nx = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(nx)] for _ in range(nx)]
    optimal = 1
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(y, x):
        if dp[y][x] != 0:
            return dp[y][x]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < nx and 0 <= new_y < ny and matrix[new_y][new_x] > matrix[y][x]:
                dp[y][x] = max(dp[y][x], dfs(new_y, new_x))
        dp[y][x] += 1
        return dp[y][x]

    for y in range(ny):
        for x in range(nx):
            optimal = max(optimal, dfs(y, x))

    return optimal
