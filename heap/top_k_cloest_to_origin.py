import heapq


# LC 973 top k closest points to origin
def k_closest(points, k):
    pq = []
    for point in points:
        d = point[0] ** 2 + point[1] ** 2
        if len(pq) >= k:
            if d < -pq[0][0]:
                heapq.heappushpop(pq, (-d, point[0], point[1]))
        else:
            heapq.heappush(pq, (-d, point[0], point[1]))
    return [[x[1], x[2]] for x in pq]
