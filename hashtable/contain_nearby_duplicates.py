from collections import defaultdict


# LC 219: contain nearby duplicates II
def contain_nearby_duplication(nums, k):
    rec = {}
    for i, num in enumerate(nums):
        if num in rec:
            if abs(i - rec[num]) <= k:
                return True
        rec[num] = i
    return False
