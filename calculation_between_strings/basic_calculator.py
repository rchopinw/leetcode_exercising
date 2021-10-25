from collections import deque


# basic calculator i
def basic_calculator_i(s):
    stack = []
    operand = 0
    res = 0  # For the on-going result
    sign = 1  # 1 means positive, -1 means negative
    for ch in s:
        if ch.isdigit():
            operand = (operand * 10) + int(ch)
        elif ch == '+':
            res += sign * operand
            sign = 1
            operand = 0
        elif ch == '-':
            res += sign * operand
            sign = -1
            operand = 0
        elif ch == '(':
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif ch == ')':
            res += sign * operand
            res *= stack.pop()  # stack pop 1, sign
            res += stack.pop()  # stack pop 2, operand
            operand = 0
    return res + sign * operand


# basic calculator ii
def basic_calculator_ii(s):
    op, res, num, pending = '+', 0, 0, 0
    for ch in s:
        if ch.isdigit():
            num = 10 * num + int(ch)
        if ch in ['+', '-', '*', '/']:
            if op == '+':
                pending += num
            elif op == '-':
                pending -= num
            elif op == '*':
                pending *= num
            elif op == '/':
                pending = int(pending/num)
            if ch in ['+', '-']:
                res += pending
                pending = 0
            op = ch
            num = 0
    return res


# basic calculator iii
def basic_calculator_iii(s):
    def helper(q):
        stack = []
        num = ''
        sign = '+'
        while q:
            x = q.popleft()
            if x == '(':
                num = helper(q)
            if x.isnumeric():
                num += x
            if not x.isnumeric() or not q:
                if sign == '+':
                    stack.append(int(num or 0))
                elif sign == '-':
                    stack.append(-1 * int(num or 0))
                elif sign == '*':
                    stack.append(stack.pop() * int(num))
                elif sign == '/':
                    stack.append(int(stack.pop() / int(num)))
                sign = x
                num = ''
            if x == ')':
                break
        return sum(stack)
    q = deque(s.replace(' ', ''))
    return help(q)
