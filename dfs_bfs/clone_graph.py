# LC 133: Clone graph
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = [] if neighbors is None else neighbors


def clone_graph(node, ):
    visited = {}

    def dfs(n):
        if not n:
            return n
        if n in visited:
            return visited[n]
        clone_n = Node(val=n.val)
        visited[n] = clone_n
        if n.neighbors:
            clone_n.neighbors = [dfs(nd) for nd in n.neighbors]
        return clone_n

    return dfs(node)

