class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, v):
    node = Node(v)

    if not head:
        node.next = node
        return node

    cur = head
    while True:
        if cur.val <= v <= cur.next.val:
            break
        if cur.val > cur.next.val:
            if v >= cur.val or v <= cur.next.val:
                break
        cur = cur.next
        if cur == head:
            break

    node.next = cur.next
    cur.next = node

    return head

