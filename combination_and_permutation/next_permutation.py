# LC 31 next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
def next_permutation(nums):
    if len(nums) < 2:
        return

    flag = -1
    for i in range(len(nums) - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            flag = i - 1
            break

    if flag == -1:
        nums.reverse()
        return

    j = len(nums) - 1
    while nums[flag] >= nums[j]:
        j -= 1
    nums[flag], nums[j] = nums[j], nums[flag]

    nums[flag + 1:] = nums[flag + 1:][::-1]