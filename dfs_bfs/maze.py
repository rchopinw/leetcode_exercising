from collections import deque


# LC 490: The maze
def has_path(maze, start, destination):
    ny, nx = len(maze), len(maze[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = {}
    queue = deque([start])
    while queue:
        y, x = queue.popleft()
        visited[y, x] = True
        if [y, x] == destination:
            return True
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            while 0 <= new_x < nx and 0 <= new_y < ny and maze[new_y][new_x] != 1:
                new_x += dx
                new_y += dy
            new_x -= dx
            new_y -= dy
            if (new_y, new_x) not in visited:
                queue.append((new_y, new_x))
                visited[new_y, new_x] = True
    return False
