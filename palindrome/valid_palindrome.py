# LC 680: Valid Palindrome
def valid_palindrome_ii(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[right] == s[left]:
            left += 1
            right -= 1
        else:
            s_left = s[:left] + s[left + 1:]
            s_right = s[:right] + s[right + 1:]
            return s_left == s_left[::-1] or s_right == s_right[::-1]
    return True
