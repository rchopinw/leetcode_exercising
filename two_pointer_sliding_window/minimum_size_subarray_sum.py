def minimum_size_subarray(nums, s):
    if not nums:
        return -1
    n = len(nums)
    optimal = n + 1
    sm = 0
    j = 0
    for i in range(n):
        while j < n and sm < s:
            sm += nums[j]
            j += 1
        if sm > s:
            optimal = min(optimal, j - i)
        sm -= nums[i]
    if optimal == n + 1:
        return -1
    return optimal
