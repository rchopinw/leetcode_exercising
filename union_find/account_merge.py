from collections import defaultdict
# LC 721, Account Merge


class UnionFind:
    def __init__(self, parents, ):
        self.parents = parents

    def find(self, x, ):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y, ):
        self.parents[self.find(x)] = self.find(y)


def account_merge(accounts):
    e_to_n = {}
    e_to_i = {}
    i = 0
    uf = UnionFind(parents=[x for x in range(10001)])
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            e_to_n[email] = name
            if email not in e_to_i:
                e_to_i[email] = i
                i += 1
            uf.union(e_to_i[account[1]], e_to_i[email])
    ans = defaultdict(list)
    for email in e_to_i:
        ans[uf.find(e_to_i[email])].append(email)
    return [[e_to_n[ans[x][0]]] + sorted(ans[x]) for x in ans]
