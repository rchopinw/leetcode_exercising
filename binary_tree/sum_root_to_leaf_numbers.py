# LC 129: Sum of all paths from root to leaf node
def sum_root_to_leaf_node(root):
    s = 0

    def dfs(node, cur):
        nonlocal s
        cur += node.val
        if node.right is None and node.left is None:
            s += int(cur)
        if node.left:
            dfs(node.left, cur)
        if node.right:
            dfs(node.right, cur)

    dfs(root, '')
    return s