# LC 56 merging intervals:
def merge_intervals(intervals):
    intervals.sort()
    results = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= results[-1][1]:
            results[-1][1] = max(interval[1], results[-1][1])
        else:
            results.append(interval)
    return results