class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# LC 426: Convert Binary Search Tree to Sorted Doubly Linked List
def convert_bst(root):
    stack = []
    head = Node(0)
    dummy = head
    cur= root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        head.right = cur
        cur.left = head
        head = cur
        cur = cur.right
    dummy.right.left = head
    head.right = dummy.right
    return dummy.right
