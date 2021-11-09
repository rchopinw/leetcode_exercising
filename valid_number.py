# LC 65 Valid Number
def valid_number(s):
    digit, dot, exponent = False, False, False
    for i, c in enumerate(s):
        if c.isdigit():
            digit = True
        elif c in ['+', '-']:
            if i > 0 and s[i - 1].upper() != 'E':
                return False
        elif c.upper() == 'E':
            if exponent or not digit:
                return False
            exponent = True
            digit = False  # in case the string is ending with E or e
        elif c == '.':
            if dot or exponent:
                return False
            dot = True
        else:
            return False
    return digit
