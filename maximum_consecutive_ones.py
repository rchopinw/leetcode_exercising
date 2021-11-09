# LC 1004: Max consecutive ones iii
def longest_ones(nums, k):
    left = 0
    for right in range(len(nums)):
        k -= 1 - nums[right]
        if k < 0:
            k += 1 - nums[left]
            left += 1
    return len(nums) - left
