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
    return flag2 - flag1 + 1 if flag2 > flag1 else 0
