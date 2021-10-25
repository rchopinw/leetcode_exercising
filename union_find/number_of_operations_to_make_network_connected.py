class UnionFind:
    def __init__(self, parents):
        self.parents = parents

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent == y_parent:
            return False
        self.parents[self.find(x)] = self.find(y)
        return True


def make_connected(n, connections):
    if n - len(connections) >= 2:
        return -1
    uf = UnionFind(parents=[x for x in range(n)])
    num_available = 0
    num_groups = set()
    for prv, nxt in connections:
        if not uf.union(prv, nxt):
            num_available += 1
    for i in range(n):
        num_groups.add(uf.find(i))
    if len(num_groups) - 1 <= num_available:
        return len(num_groups) - 1
    return -1

