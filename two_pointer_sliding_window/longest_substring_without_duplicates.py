# LC 3: longest substring without repeating characters
def longest_substring_without_repeating(s):
    left, right, rec, optimal = 0, 0, {}, 0
    while right < len(s):
        if s[right] in rec and rec[s[right]] >= left:
            left = rec[s[right]] + 1
        rec[s[right]] = right
        optimal = max(optimal, right - left + 1)
        right += 1
    return optimal

