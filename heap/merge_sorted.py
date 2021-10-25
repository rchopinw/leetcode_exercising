import heapq


# LC 21: Merge 2 lists
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def merge_two_lists(l1, l2):
    m = ListNode()
    cur = m
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
    return m.next


# LC 23: Merge K sorted lists
def merge_k_sorted_lists(lists):
    pq = []
    m = ListNode()
    cur = m
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(pq, (l.val, i))
            lists[i] = lists[i].next
    while pq:
        cur_val, f = heapq.heappop(pq)
        cur.next = ListNode(val=cur_val)
        if lists[f]:
            heapq.heappush(pq, (lists[f].val, f))
            lists[f] = lists[f].next
        cur = cur.next
    return m.next


# LC 88: Merge sorted array
def merge_sorted(nums1, m, nums2, n):
    p, p1, p2 = 0, 0, 0
    nums3 = nums1[:m]
    while p1 < m and p2 < n:
        if nums3[p1] < nums2[p2]:
            nums1[p] = nums3[p1]
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1
        p += 1
    while p < m + n and p1 < m:
        nums1[p] = nums3[p1]
        p1 += 1
        p += 1
    while p < m + n and p2 < n:
        nums1[p] = nums2[p2]
        p2 += 1
        p += 1