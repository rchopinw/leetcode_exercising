# LC 259: 3 sum smaller
def two_sum_smaller(nums, left, right, t):
    c = 0
    while left < right:
        if nums[left] + nums[right] < t:
            c += right - left
            left += 1
        else:
            right -= 1
    return c


def three_sum_smaller(nums, k):
    """
    Time Complexity: O(Nlog(N)) + O(N^2) = O(N^2)
    Space Complexity: O(1)
    :param nums:
    :param k:
    :return:
    """
    if len(nums) < 3:
        return 0

    count = 0
    nums.sort()

    for i in range(len(nums) - 2):
        count += two_sum_smaller(nums, i + 1, len(nums) - 1, k - nums[i])

    return count

