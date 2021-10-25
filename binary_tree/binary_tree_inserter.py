from collections import deque


# LC 919 Complete binary tree inserter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root):
        self.root = root
        self.q = self._find_node()

    def insert(self, val: int) -> int:
        node = TreeNode(val=val)
        cur = self.q[0]
        if cur.left is None:
            cur.left = node
        elif cur.right is None:
            cur.right = node
            self.q.append(cur.left)
            self.q.append(cur.right)
            self.q.popleft()
        return cur.val

    def get_root(self):
        return self.root

    def _find_node(self, ):
        queue = deque([self.root])
        while queue:
            cur = queue[0]
            if cur.left and cur.right:
                queue.append(cur.left)
                queue.append(cur.right)
                queue.popleft()
            else:
                break
        return queue
