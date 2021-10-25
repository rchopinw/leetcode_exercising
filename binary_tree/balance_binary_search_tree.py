# LC 1382: Balance a binary search tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balance_bst(root):
    l = []

    def in_order(node):
        if node is None:
            return
        in_order(node.left)
        l.append(node)
        in_order(node.right)

    def build(left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = l[mid]
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    in_order(root)
    return build(0, len(l) - 1)
