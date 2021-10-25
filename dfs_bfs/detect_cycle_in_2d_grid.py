from collections import deque


# LC 1559: Detect Cycles in 2D Grid
def detect_cycles(grid):
    ny, nx = len(grid), len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    mk = '0'

    def bfs(y, x, symbol, mark):
        visited = {(y, x): 0}
        queue = deque([(y, x, None)])
        while queue:
            cur_y, cur_x, prev = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = cur_x + dx, cur_y + dy
                if (new_y, new_x) in visited and (new_y, new_x) != prev:
                    return True
                if 0 <= new_x < nx and 0 <= new_y < ny:
                    if (new_y, new_x) not in visited and grid[new_y][new_x] == symbol:
                        grid[new_y][new_x] = mark
                        visited[new_y, new_x] = 0
                        queue.append((new_y, new_x, (cur_y, cur_x)))
        return False

    for y in range(ny):
        for x in range(nx):
            if grid[y][x].isalpha():
                sym = grid[y][x]
                if bfs(y, x, sym, mk):
                    return True
    return False
