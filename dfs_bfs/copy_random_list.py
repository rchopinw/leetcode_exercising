class Node:
    def __init__(self, x, next_=None, random=None):
        self.val = int(x)
        self.next = next_
        self.random = random


def copy_random_list(head):
    node_rec = {}

    def dfs(node):
        if not node:
            return node
        if node in node_rec:
            return node_rec[node]
        new_node = Node(x=node.val)
        node_rec[node] = new_node
        if node.next:
            new_node.next = dfs(node.next)
        if node.random:
            new_node.random = dfs(node.random)
        return new_node

    return dfs(head)
