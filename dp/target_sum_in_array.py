# LC 494: TARGET SUM
def target_sum(nums, target):
    dp = {}

    def backtrack(idx, s):
        if idx == len(nums):
            return 1 if s == target else 0
        dp[idx, s] = backtrack(idx + 1, s - nums[idx]) + backtrack(idx + 1, s + nums[idx])
        return dp[idx, s]

    return backtrack(0, 0)


def target_sum_ii(nums, target):
    """
    Time Complexity: O(t * n)
    Space Complexity: O(t)
    since the sum can range from -total to total, where total equals to the sum of the nums array,
    we need to add an offset of total to the sum indices (column number) to map
    all the sums obtained to positive range only.
    :param nums:
    :param target:
    :return:
    """
    s = sum(nums)
    dp = [0 for _ in range(2 * s + 1)]
    dp[s - nums[0]] += 1
    dp[s + nums[0]] += 1
    for num in nums[1:]:
        new_dp = [0 for _ in range(2 * s + 1)]
        for new_s in range(-s, s + 1, 1):
            if dp[new_s + s] > 0:
                new_dp[new_s + num + s] += dp[new_s + s]
                new_dp[new_s - num + s] += dp[new_s + s]
        dp = new_dp
    return 0 if abs(target) > s else dp[target + s]