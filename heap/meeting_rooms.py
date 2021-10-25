import heapq


def meeting_rooms_ii(intervals):
    intervals.sort()
    pq = [intervals[0][1]]
    for interval in intervals[1:]:
        if pq and interval[0] >= pq[0]:
            heapq.heappop(pq)
        heapq.heappush(pq, interval[1])
    return len(pq)
