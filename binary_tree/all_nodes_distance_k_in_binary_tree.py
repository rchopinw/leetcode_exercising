from collections import defaultdict, deque


# LC 863 All nodes distance k in binary tree
def distance_k(root, target, k):
    adj = defaultdict(list)

    def dfs(node, parent):
        if node:
            if parent:
                adj[node.val].append(parent)
            if node.left:
                adj[node.val].append(node.left.val)
            if node.right:
                adj[node.val].append(node.right.val)
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root, None)

    queue = deque([(target.val, 0)])
    visited = {target.val}
    results = []
    while queue:
        cur_val, cur_dist = queue.popleft()
        if cur_dist == k:
            results.append(cur_val)
            continue
        for nei in adj[cur_val]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, cur_dist + 1))
    return results

