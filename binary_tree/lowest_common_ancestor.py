# LC 236: lowest common ancestor in a binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    res = None
    def dfs(node):
        nonlocal res
        if node is None:
            return False
        left = dfs(node.left)
        right = dfs(node.right)
        mid = p == node or q == node
        if mid + right + left >= 2:
            res = node
        return mid or right or left
    dfs(root)
    return res


def lowest_common_ancestor_ii(p, q):
    def dfs(node1, node2, set1, set2):
        if node1:
            set1.add(node1)
        if node2:
            set2.add(node2)
        if node1 in set2:
            return node1
        if node2 in set1:
            return node2
        return dfs(node1.parent if node1 else node1, node2.parent if node2 else node2, set1, set2)

    return dfs(p, q, set(), set())