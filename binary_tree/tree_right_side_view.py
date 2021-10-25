# LC 199: rightside view
def right_side_view(root):
    result = []
    if not root:
        return result
    queue = [root]
    while queue:
        result.append(queue[-1].val)
        new_queue = []
        for node in queue:
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        queue = new_queue
    return result