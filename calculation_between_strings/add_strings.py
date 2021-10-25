# LC 415: add strings
def add_strings(num1, num2):
    add, res = 0, ''
    num1, num2 = list(num1), list(num2)
    while num1 and num2:
        cur_sum = int(num1.pop()) + int(num2.pop()) + add
        add = 1 if cur_sum > 9 else 0
        res += str(cur_sum)[-1]
    while num1:
        cur_sum = int(num1.pop()) + add
        add = 1 if cur_sum > 9 else 0
        res += str(cur_sum)[-1]
    while num2:
        cur_sum = int(num2.pop()) + add
        add = 1 if cur_sum > 9 else 0
        res += str(cur_sum)[-1]
    if add:
        res += str(add)
    return res[::-1]
