import itertools
from collections import defaultdict


def count_corner_rectangles(grid):
    """
    Time Complexity: O(R * C^2)
    Space Complexity: O(C^2)
    :param grid:
    :return:
    """
    total, dp = 0, defaultdict(int)
    for row in grid:
        for c1, v1 in enumerate(row):
            if v1:
                for c2, v2 in enumerate(row[c1 + 1:]):
                    if v2:
                        total += dp[c1, c2]
                        dp[c1, c2] += 1
    return total


def count_corner_rectangles_ii(grid):
    """
    Time Complexity: O(N * sqrt(N) + R * C)
    Space Complexity: O(N + R + C^2)
    :param grid:
    :return:
    """
    rows = [[c for c, v in enumerate(row) if v] for row in grid]
    n = sum(len(row) for row in grid)
    threshold = int(n**0.5)
    ans = 0
    dp = defaultdict(int)
    for r, row in enumerate(rows):
        if len(row) >= threshold:
            target = set(row)
            for r2, row2 in enumerate(rows):
                if r2 <= r and len(row2) >= threshold:
                    continue
                found = sum(1 for c2 in row2 if c2 in target)
                ans += (found - 1) * found / 2
        else:
            for pair in itertools.combinations(row, 2):
                ans += dp[pair]
                dp[pair] += 1
    return ans
