# LC 921: min add to make parentheses valid
def min_add(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack[-1] == ')':
                stack.pop()
            else:
                stack.append(c)
    return len(stack)


def min_add_parentheses_ii(s):
    total, right = 0, 0
    for c in s:
        right += 1 if c == '(' else -1
        if right == -1:  # means we need to add ( parentheses on the left side
            total += 1
            right += 1
    return total + right  # right means the ) parentheses needed
