from collections import defaultdict, deque


# LC 827 Making a large island
def largest_island(grid):
    ny, nx = len(grid), len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    island_sizes = defaultdict(int)
    island_id = 1
    for y in range(ny):
        for x in range(nx):
            if grid[y][x] == 1:
                island_id += 1
                island_sizes[island_id] += 1
                grid[y][x] = island_id
                queue = deque([(y, x)])
                while queue:
                    cur_y, cur_x = queue.popleft()
                    for dx, dy in directions:
                        new_x, new_y = cur_x + dx, cur_y + dy
                        if 0 <= new_x < nx and 0 <= new_y < ny and 0 < grid[new_y][new_x] < island_id:
                            queue.append((new_y, new_x))
                            island_sizes[island_id] += 1
                            grid[new_y][new_x] = island_id
    optimal = 0
    for y in range(ny):
        for x in range(nx):
            if grid[y][x] == 0:
                adj = set()
                for dx, dy in directions:
                    if 0 <= x + dx < nx and 0 <= y + dy < dy and grid[y + dy][x + dx] > 0:
                        adj.add(grid[y + dy][x + dx])
                optimal = max(optimal, 1 + sum(island_sizes[x] for x in adj))
    return optimal if optimal else nx * ny