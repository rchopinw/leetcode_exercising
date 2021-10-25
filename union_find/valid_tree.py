from collections import defaultdict


# LC 261 Valid Graph Tree
def valid_graph_tree(n, edges):
    if len(edges) != n - 1:
        return False

    rec = defaultdict(list)
    for x, y in edges:
        rec[x].append(y)
        rec[y].append(x)

    visited = {}

    def dfs(node):
        if node in visited:
            return
        visited[node] = 1
        for x in rec[node]:
            dfs(x)

    dfs(0)

    return len(visited) == n


# Union find solution
class UnionFind:
    def __init__(self, parents):
        self.parents = parents

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)


def valid_tree(n, edges):
    if n - len(edges) != 1:
        return False
    uf = UnionFind(parents=[x for x in range(n)])
    for node1, node2 in edges:
        uf.union(node1, node2)
    parents = set()
    for i in uf.parents:
        parents.add(uf.find(i))
    return len(parents) == 1

