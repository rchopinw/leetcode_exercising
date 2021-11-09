# LC 71 Simplify path
def simplify_path(path):
    stack = []
    for symbol in path.split('/'):
        if not symbol or symbol == '.':
            continue
        elif symbol == "..":
            if stack:
                stack.pop()
        else:
            stack.append(symbol)
    return '/' + '/'.join(stack)