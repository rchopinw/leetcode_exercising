# LC 17: letter combinatino of a phone number
def letter_combination(digits):
    m = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    res = []
    if not digits:
        return res
    res += m[digits[0]]
    for digit in digits[1:]:
        new = []
        for d in m[digit]:
            new.extend([x + d for x in res])
        res = new
    return res
