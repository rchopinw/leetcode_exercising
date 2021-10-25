from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


def delete_node_from_tree(root, to_delete):
    to_delete = set(to_delete)
    res = []
    queue = deque([root, True])
    while queue:
        cur, flag = queue.popleft()
        if cur.left:
            queue.append((cur.left, cur.val in to_delete))
            if cur.left.val in to_delete:
                cur.left = None
        if cur.right:
            queue.append((cur.right, cur.val in to_delete))
            if cur.right.val in to_delete:
                cur.right = None
        if cur.val not in to_delete and flag:
            res.append(cur)
    return res
