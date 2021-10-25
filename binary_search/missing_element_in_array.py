# LC 1060: Missing element in an array
def binary_search(nums, k):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if k > nums[mid]:
            left = mid + 1
        else:
            right = mid
    return left


def missing_element_in_array(nums, k):
    diff, s = [], 0
    for i in range(1, len(nums)):
        s += nums[i] - nums[i - 1]
        diff.append(s)
    pos = binary_search(diff, k)
    return nums[pos] + k if pos == 0 else nums[pos] + k - diff[pos - 1]
