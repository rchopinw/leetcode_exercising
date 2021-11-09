# LC 581: Find unsorted continuous subarray
def find_unsorted_continuous(nums):
    stack1, stack2 = [], []
    flag1, flag2 = len(nums), 0
    for i, (num1, num2) in enumerate(zip(nums, nums[::-1])):
        while stack1 and num1 < nums[stack1[-1]]:
            flag1 = min(flag1, stack1.pop())
        while stack2 and num2 > nums[stack2[-1]]:
            flag2 = max(flag2, stack2.pop())
        stack1.append(i)
        stack2.append(len(nums) - i - 1)
    print(flag1, flag2)
    return flag2 - flag1 + 1 if flag2 > flag1 else 0


def find_unsorted_continuous_ii(nums):
    min_, max_ = float('inf'), float('-inf')
    left, right = len(nums), 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            min_ = min(min_, nums[i])
        if nums[len(nums) - i] < nums[len(nums) - i - 1]:
            max_ = max(max_, nums[len(nums) - i - 1])
    for i, num in enumerate(nums):
        if num > min_:
            left = min(left, i)
        if nums[len(nums) - i - 1] < max_:
            right = max(right, len(nums) - i - 1)
    return right - left + 1 if right > left else 0

