from collections import defaultdict


# LC 560 subarray sum
def sub_array_sum(nums, k):
    count, prefix, cur_sum = 0, defaultdict(int), 0
    for num in nums:
        cur_sum += num
        count += (cur_sum == k) + prefix[cur_sum - k]
        prefix[cur_sum] += 1
    return count
