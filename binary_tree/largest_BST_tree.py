# LC 333: Largest BST Tree
def largest_bst_tree(root):
    if not root:
        return 0
    optimal = float('-inf')

    def dfs(node):
        nonlocal optimal
        if node is None:
            return True, float('-inf'), float('inf'), 0
        li, lmax, lmin, ll = dfs(node.left)
        ri, rmax, rmin, rl = dfs(node.right)
        cur_i = True
        if li and ri:
            if node.left and node.val <= lmax:
                cur_i = False
            if node.right and node.val >= rmin:
                cur_i = False
            if cur_i:
                optimal = max(optimal, ll + rl + 1)
                return True, max(lmax, rmax, node.val), min(lmin, rmin, node.val), ll + rl + 1
        return False, float('-inf'), float('inf'), 0

    dfs(root)

    return optimal
