from collections import deque


def min_push(grid):
    ny, nx = len(grid), len(grid[0])
    box, person, target = (), (), ()
    for y in range(ny):
        for x in range(nx):
            if grid[y][x] == 'B':
                box = (y, x)
            elif grid[y][x] == 'S':
                person = (y, x)
            elif grid[y][x] == 'T':
                target = (y, x)

    def is_valid(y, x):
        return 0 <= y < ny and 0 <= x < nx and grid[y][x] != '#'

    def can_move(f, t, b):
        queue = deque([f])
        visited = set()
        while queue:
            cur = queue.popleft()
            if cur == t:
                return True
            for y, x in [(cur[0] + 1, cur[1]), (cur[0] - 1, cur[1]), (cur[0], cur[1] + 1), (cur[0], cur[1] - 1)]:
                if is_valid(y, x) and (y, x) != b and (y, x) not in visited:
                    visited.add((y, x))
                    queue.append((y, x))
        return False

    q = deque([(0, box, person)])
    visited = {box + person}
    while q:
        cur_dist, cur_box, cur_person = q.popleft()
        if cur_box == target:
            return cur_dist
        box_pos = [(cur_box[0] + 1, cur_box[1]), (cur_box[0] - 1, cur_box[1]),
                   (cur_box[0], cur_box[1] + 1), (cur_box[0], cur_box[1] - 1)]
        person_pos = [(cur_box[0] - 1, cur_box[1]), (cur_box[0] + 1, cur_box[1]),
                      (cur_box[0], cur_box[1] - 1), (cur_box[0], cur_box[1] + 1)]
        for nb, np in zip(box_pos, person_pos):
            if is_valid(*nb) and (cur_box + nb) not in visited and is_valid(*np) and can_move(cur_person, np, cur_box):
                q.append((cur_dist + 1, nb, cur_box))
                visited.add((cur_box + nb))

