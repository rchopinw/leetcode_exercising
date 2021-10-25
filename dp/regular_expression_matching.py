# LC 10 Regular Expression Matching
def regular_expression_matching(s, p):
    dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
    dp[-1][-1] = True
    for y in range(len(s), -1, -1):
        for x in range(len(p) - 1, -1, -1):
            first_match = y < len(s) and (p[x] == s[y] or p[x] == '.')
            if x + 1 < len(p) and p[x + 1] == "*":
                dp[y][x] = dp[y][x + 2] or first_match and dp[y + 1][x]
            else:
                dp[y][x] = first_match and dp[y + 1][x + 1]
    return dp[0][0]

