from collections import Counter
import heapq


# LC 347 top k frequent
def top_k_frequent(nums, k):
    pq = []
    count = Counter(nums)
    for pair in count.items():
        if len(pq) >= k:
            if (pair[1], pair[0]) > pq[0]:
                heapq.heappushpop(pq, (pair[1], pair[0]))
        else:
            heapq.heappush(pq, (pair[1], pair[0]))
    return [heapq.heappop(pq)[1] for _ in range(k)]