from collections import Counter
import heapq


# LC 767: Reorganize string
def reorganize_string(s):
    i = 0
    count = Counter(s)
    ans = ["" for _ in range(len(s))]
    pq = [(-y, x) for x, y in count.items()]
    heapq.heapify(pq)
    if -pq[0][0] > (len(s) + 1) // 2:
        return ""
    while pq:
        ct, ch = heapq.heappop(pq)
        for j in range(-ct):
            ans[i] = ch
            i += 2
            if i >= len(s):
                i = 1
    return ''.join(ans)

