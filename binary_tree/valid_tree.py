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
