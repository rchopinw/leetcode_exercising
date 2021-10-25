# LC 907 sum of subarray minimums
def sum_of_subarray(arr):
    stack = []
    dp = [0 for _ in range(len(arr))]
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] > num:
            stack.pop()
        if stack:
            dp[i] = dp[stack[-1]] + num * (i - stack[-1])
        else:
            dp[i] = num * (i + 1)
    return sum(dp)
