# LC 298: Longest consecutive sequence
def longest_consecutive_sequence(root):
    optimal = 0
    def dfs(node, length):
        nonlocal optimal
        if node.right:
            if node.right.val - node.val == 1:
                dfs(node.right, length + 1)
            else:
                dfs(node.right, 1)
        if node.left:
            if node.left.val - node.val == 1:
                dfs(node.left, length + 1)
            else:
                dfs(node.left, 1)
        optimal = max(optimal, length)
    dfs(root, 1)
    return optimal

