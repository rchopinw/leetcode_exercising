# LC 15: 3 sum
def three_sum(nums):
    res = []
    nums.sort()

    def two_sum(i):
        left, right = i + 1, len(nums) - 1
        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if cur_sum < 0:
                left += 1
            elif cur_sum > 0:
                right -= 1
            else:
                left += 1
                right -= 1
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i] != nums[i - 1]:
            two_sum(i)

    return res
