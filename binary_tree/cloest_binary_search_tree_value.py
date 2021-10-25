# LC 270: cloest binary search tree value
def cloest_bst(root, target):
    min_dist = root.val

    def dfs(node):
        nonlocal min_dist
        if node is None:
            return
        if abs(target - min_dist) > abs(target - node.val):
            min_dist = node.val
        if target > node.val:
            dfs(node.right)
        else:
            dfs(node.left)

    dfs(root)
    return min_dist
