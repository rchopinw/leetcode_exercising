# LC 515: Find largest value in each tree row
def find_largest_in_each_row(root):
    if root is None:
        return []
    stack = [root]
    results = [root.val]
    while stack:
        new_stack = []
        optimal = float('-inf')
        for node in stack:
            if node.left:
                optimal = max(optimal, node.left.val)
                new_stack.append(node.left)
            if node.right:
                optimal = max(optimal, node.right.val)
                new_stack.append(node.right)
        results.append(optimal)
        stack = new_stack
    return results[:-1]
