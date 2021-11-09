import heapq


# LC 1353 Maximum number of events can be attended
def maximum_event(events):
    """
    1. Add events start with day i (today)
    2. Remove events end before day i (today)
    3. Attend one event on day i (today)
    :param events:
    :return:
    """
    pq = []
    p = 0  # record the events
    attend = 0
    events.sort()
    max_days = max(x[1] for x in events)
    for today in range(1, max_days + 1):
        while len(events) > p and today == events[p][0]:
            heapq.heappush(pq, events[p][1])
            p += 1
        while pq and pq[0] < today:
            heapq.heappop(pq)
        if pq:
            heapq.heappop(pq)
            attend += 1
    return attend
