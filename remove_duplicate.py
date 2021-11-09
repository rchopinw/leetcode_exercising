# LC 1047: remove duplicates:
def remove_duplicates(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


def remove_duplicates_ii(s: str, k: int) -> str:
    stack = []

    for c in s:
        if not stack or stack[-1][0]!=c:
            stack.append([c, 1])
        elif stack[-1][0] == c:
            stack.append([c, stack[-1][1]+1])
        if stack[-1][1] == k:
            n = k
            while n:
                stack.pop()
                n -= 1
    return "".join([a[0] for a in stack])
