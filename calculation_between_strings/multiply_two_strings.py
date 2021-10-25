# LC 43: Multiply strings
def multiply_strings(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    num1 = num1[::-1]
    num2 = num2[::-1]
    total_len = len(num1) + len(num2)
    result = [0 for _ in range(total_len)]
    for i, d1 in enumerate(num1):
        for j, d2 in enumerate(num2):
            zeros = i + j
            add_pos = result[zeros]
            multi_plus = int(d1) * int(d2) + add_pos
            result[zeros], result[zeros + 1] = multi_plus % 10, multi_plus // 10
    while result[-1] == 0:
        result.pop()
    return ''.join(str(x) for x in result[::-1])

