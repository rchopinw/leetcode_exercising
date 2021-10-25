from collections import defaultdict


def count_corner_rectangles(grid):
    total, dp = 0, defaultdict(int)
    for row in grid:
        for c1, v1 in enumerate(row):
            if v1:
                for c2, v2 in enumerate(row[c1 + 1:]):
                    if v2:
                        total += dp[c1, c2]
                        dp[c1, c2] += 1
    return total
