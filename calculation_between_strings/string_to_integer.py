# LC 8: string to integer
def string_to_integer(s):
    if not s:
        return 0

    while s and s[0] == ' ':
        s = s[1:]

    if not s or s[0].isalpha():
        return 0

    res = ''

    operand = "+"

    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

    if s[0] in ['+', '-']:
        operand = s[0]
        s = s[1:]

    for c in s:
        if c.isdigit():
            res += c
        else:
            break
    if not res:
        return 0
    res = -1 * int(res) if operand == '-' else int(res)
    if res < INT_MIN:
        return INT_MIN
    elif res > INT_MAX:
        return INT_MAX
    else:
        return res
