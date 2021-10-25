# LC 938 Range sum of a BST
def range_sum(root, low: int, high: int) -> int:
    ans = 0

    def dfs(node):
        nonlocal ans
        if not node:
            return
        if low <= node.val <= high:
            ans += node.val
        if node.val > high:
            dfs(node.left)
        elif node.val < low:
            dfs(node.right)
        else:
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return ans
