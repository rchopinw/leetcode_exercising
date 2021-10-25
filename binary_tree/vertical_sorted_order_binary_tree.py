from collections import defaultdict


# LC 987: Vertical Traversal
from collections import deque


def vertical_traversal(root):
    if not root:
        return []
    queue = deque([(root, 0, 0)])
    rec = defaultdict(list)
    while queue:
        node, x, y = queue.popleft()
        rec[x].append((y, node.val))
        if node.left:
            queue.append((node.left, x - 1, y + 1))
        if node.right:
            queue.append((node.right, x + 1, y + 1))
    return [[y[1] for y in sorted(rec[x])] for x in sorted(rec)]
