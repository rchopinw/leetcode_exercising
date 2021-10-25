# LC 523
def check_sub_array_sum(nums, k):
    prefix, s = {0: -1}, 0
    for i, num in enumerate(nums):
        s += num
        if s % k in prefix:
            if i - prefix[s % k] >= 2:
                return True
        else:
            prefix[s % k] = i
    return False
