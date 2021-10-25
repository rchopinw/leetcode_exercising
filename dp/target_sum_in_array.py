# LC 494: TARGET SUM
def target_sum(nums, target):
    dp = {}

    def backtrack(idx, s):
        if idx == len(nums):
            return 1 if s == target else 0
        dp[idx, s] = backtrack(idx + 1, s - nums[idx]) + backtrack(idx + 1, s + nums[idx])
        return dp[idx, s]

    return backtrack(0, 0)
