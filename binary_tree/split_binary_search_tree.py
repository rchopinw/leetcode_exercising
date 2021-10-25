class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# LC 776: split binary search tree
def split_binary_search_tree(root, target):

    def split(node, left, right):
        if node is None:
            return
        if node.val > target:
            right.left = TreeNode(node.val, right=node.right)
            return split(node.left, left, right.left)
        else:
            left.right = TreeNode(node.val, left=node.left)
            return split(node.right, left.right, right)

    d_left, d_right = TreeNode(0), TreeNode(0)

    split(root, d_left, d_right)

    return d_left.right, d_right.left
