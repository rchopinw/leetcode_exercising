from collections import Counter, defaultdict


# LC 76: Minimum window substring
def minimum_window(s, t):
    left, right, optimal, optimal_s = 0, 0, len(s) + 1, ''
    t_count = Counter(t)
    c_count = defaultdict(int)
    formulated = 0
    while right < len(s):
        c = s[right]
        c_count[c] += 1
        if c in t_count and t_count[c] == c_count[c]:
            formulated += 1
        while formulated == len(t_count) and left <= right:
            c = s[left]
            if right - left + 1 < optimal:
                optimal, optimal_s = right - left + 1, s[left:right+1]
            c_count[c] -= 1
            if c in t_count and t_count[c] > c_count[c]:
                formulated -= 1
            right += 1
        left += 1
    return optimal_s


