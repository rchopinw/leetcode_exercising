from collections import deque


# LC 752: Open lock
def open_lock(deadends, target):
    deadends = set(deadends)
    if target in deadends or '0000' in deadends:
        return -1
    visited = {'0000'}
    queue = deque([('0000', 0)])
    while queue:
        cur, step = queue.popleft()
        if cur == target:
            return step
        if cur in deadends:
            continue
        for i in range(len(cur)):
            for d in [-1, 1]:
                new = cur[:i] + str((int(cur[i]) + d) % 10) + cur[i+1:]
                if new not in visited:
                    visited.add(new)
                    queue.append((new, step + 1))
    return -1
