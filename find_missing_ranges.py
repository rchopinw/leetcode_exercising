# LC 163 Find missing ranges
def find_missing_range(nums, lower, upper):
    if not nums:
        if lower == upper:
            return [str(lower)]
        else:
            return [str(lower) + '->' + str(upper)]
    res = []

    if lower < nums[0] - 1:
        res.append(str(lower) + '->' + str(nums[0] - 1))
    elif lower == nums[0] - 1:
        res.append(str(lower))

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1] + 2:
            res.append(str(nums[i - 1] + 1) + '->' + str(nums[i] - 1))
        elif nums[i] == nums[i - 1] + 2:
            res.append(str(nums[i] - 1))

    if upper > nums[-1] + 1:
        res.append(str(nums[-1] + 1) + '->' + str(upper))
    elif upper == nums[-1] + 1:
        res.append(str(nums[-1] + 1))

    return res
