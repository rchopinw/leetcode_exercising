# LC 1249 Min remove to make valid parentheses
def min_remove_valid_parentheses(s):
    stack = []
    for i, c in enumerate(s):
        if c.isalpha():
            continue
        if stack and s[stack[-1]] + c == '()':
            stack.pop()
        else:
            stack.append(i)
    s = list(s)
    for _, i in enumerate(stack):
        s[i] = ''
    return ''.join(s)
