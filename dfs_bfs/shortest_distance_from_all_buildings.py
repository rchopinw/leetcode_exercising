from collections import deque


# LC 317: shortest distance from all buildings
def shortest_distance_from_buildings(grid):
    i = 0
    ny, nx = len(grid), len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[0 for _ in range(nx)] for _ in range(ny)]

    def bfs(y, x, mark):
        optimal = float('inf')
        queue = deque([(y, x, 0)])
        while queue:
            cur_y, cur_x, cur_dist = queue.popleft()
            for dx, dy in directions:
                new_x, new_y, new_dist = cur_x + dx, cur_y + dy, cur_dist + 1
                if 0 <= new_x < nx and 0 <= new_y < ny and grid[new_y][new_x] == mark:
                    queue.append((new_y, new_x, new_dist))
                    visited[new_y][new_x] += new_dist
                    optimal = min(optimal, visited[new_y][new_x])
                    grid[new_y][new_x] -= 1
        return optimal

    optimal = -1

    for y in range(ny):
        for x in range(nx):
            if grid[y][x] == 1:
                optimal = bfs(y, x, i)
                i -= 1
                if optimal == float('inf'):
                    return -1

    return optimal
