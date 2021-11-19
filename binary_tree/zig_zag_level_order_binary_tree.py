# LC 103: zigzag level order
def zigzag_level_order(root):
    if root is None:
        return []
    stack = [root]
    results, i = [[root.val]], 1
    while stack:
        new_stack = []
        for node in stack:
            if node.left:
                new_stack.append(node.left)
            if node.right:
                new_stack.append(node.right)
        results.append(
            [x.val for x in new_stack[::-1]]
            if i % 2 else
            [x.val for x in new_stack]
        )
        i += 1
        stack = new_stack
    return results[:-1]
