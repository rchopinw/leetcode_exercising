from collections import defaultdict, deque


# LC 314: Vertical Order
def vertical_order(root):
    if not root:
        return []
    r = defaultdict(list)
    queue = deque([(root, 0)])
    while queue:
        cur_node, cur_x = queue.popleft()
        r[cur_x].append(cur_node.val)
        if cur_node.left:
            queue.append((cur_node.left, cur_x - 1))
        if cur_node.right:
            queue.append((cur_node.right, cur_x + 1))
    return [r[x] for x in sorted(r)]
