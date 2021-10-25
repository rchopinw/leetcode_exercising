# LC 206: Reversed linked list
def reverse_linked_list(head):
    if not head or not head.next:
        return head
    res, cur = [], head
    while cur:
        res.append(cur)
        cur = cur.next
    new_node = res.pop()
    cur = new_node
    while res:
        cur.next = res.pop()
        cur = cur.next
    cur.next = None
    return new_node
