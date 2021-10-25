# LC 543: DIAMETER OF BINARY TREE
def diameter_of_binary_tree(root):
    optimal = 0

    def dfs(node, n):
        nonlocal optimal
        if node is None:
            return 0
        n += 1
        left = dfs(node.left, n)
        right = dfs(node.right, n)
        optimal = max(optimal, left + right)
        return 1 + max(left, right)

    dfs(root, 0)
    return optimal
