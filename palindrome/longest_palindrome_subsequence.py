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
