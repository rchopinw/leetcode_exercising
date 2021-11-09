# LC 516: Longest palindrome subsequence
def longest_palindrome_subsequence(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    res, i = 0, 0
    while i < len(s):
        j, k = 0, i
        while j < len(s) and k < len(s):
            if j == k:
                dp[j][k] = 1
            elif k - j == 1:
                if s[j] == s[k]:
                    dp[j][k] = 2
                else:
                    dp[j][k] = 1
            else:
                if s[j] == s[k]:
                    dp[j][k] = max(max(dp[j + 1][k], dp[j][k - 1]), dp[j + 1][k - 1] + 2)
                else:
                    dp[j][k] = max(max(dp[j + 1][k], dp[j][k - 1]), dp[j + 1][k - 1])
            res = max(res, dp[j][k])
            j += 1
            k += 1
        i += 1
    return res


def longest_palindrome_subsequence_ii(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for l in range(1, len(s) + 1):
        for left in range(len(s) - l + 1):
            right = left + l - 1
            if left == right:
                dp[left][right] = 1
            elif s[left] == s[right]:
                dp[left][right] = dp[left + 1][right - 1] + 2
            else:
                dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])
    return dp[0][-1]

