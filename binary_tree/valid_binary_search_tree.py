# LC 98: Valid Binary Search Tree
def valid_bst(root):
    def dfs(node, min_, max_):
        if node is None:
            return True
        if node.val <= min_ or node.val >= max_:
            return False
        return dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_)
    return dfs(root, float('-inf'), float('inf'))



