from collections import deque


# LC 145: post-order traversal of a binary tree
def postorder_traversal(root):
    vals, pre, stack = [], None, deque()
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack[-1].right
        if not root or root is pre:
            root, pre = None, stack.pop()
            vals.append(pre.val)
    return vals


def preorder_traversal(root):
    if root is None:
        return []

    stack, output = [root, ], []

    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

    return output


def inorder_traversal(root):
    cur, ans, stack = root, [], []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        ans.append(cur.val)
        cur = cur.right
    return ans

