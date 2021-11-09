from collections import deque


def max_sliding_window(nums, k):
    if k == 1:
        return nums
    if len(nums) <= k:
        return [max(nums)]

    results, queue = [], deque([])

    for i in range(k):
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)
    results.append(nums[queue[0]])

    for i in range(k, len(nums)):
        if queue and i - queue[0] >= k:
            queue.popleft()
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)
        results.append(nums[queue[0]])

    return results

