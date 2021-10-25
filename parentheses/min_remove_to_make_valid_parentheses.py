# LC 1249 Min remove to make valid parentheses
def min_remove_valid_parentheses(s):
    stack = []
    flag = False
    for i, c in enumerate(s):
        if c.isalpha():
            continue
        elif c == '(':
            stack.append((i, c))
        else:
            if stack and stack[-1][1] == '(':
                stack.pop()
            else:
                stack.append((i, c))
    s = list(s)
    for i, _ in stack:
        s[i] = ''
    return ''.join(s)
