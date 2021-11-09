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


def k_closest_ii(points, k):
    """
    Quick select version
    Time complexity: O(N) in general, O(N^2) worst case
    Space complexity: O(N)
    :param points:
    :param k:
    :return:
    """
    distances = []
    for point in points:
        distances.append(
            (point[0]**2 + point[1]**2, point)
        )

    def quick_select(left, right):
        pivot, p = distances[right], left
        for i in range(left, right):
            if distances[i][0] < pivot[0]:
                distances[i], distances[p] = distances[p], distances[i]
                p += 1
        distances[p], distances[right] = distances[right], distances[p]
        if p == k - 1:
            return
        if p < k - 1:
            quick_select(p + 1, right)
        else:
            quick_select(left, p - 1)
    quick_select(0, len(distances) - 1)
    return [distances[i][1] for i in range(0, k)]

