# LC 124 binary tree maximum path sum
class TreeNode:
    def __init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maximum_binary_tree_path_sum(root):
    optimal = float('-inf')

    def dfs(node):
        nonlocal optimal
        if not node:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        optimal = max(optimal, left + right + node.val)
        return node.val + max(left, right)

    dfs(root)
    return optimal
