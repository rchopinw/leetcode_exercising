# LC 173: binary search tree iterator
class BSTIterator:

    def __init__(self, root):
        self.results = []
        self._dfs(root)
        self.pointer = -1

    def next(self) -> int:
        self.pointer += 1
        return self.results[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.results)

    def _dfs(self, node):
        if not node:
            return
        self._dfs(node.left)
        self.results.append(node.val)
        self._dfs(node.right)