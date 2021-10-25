# LC 282: Expression add operators
def add_operators(num, target):
    res = []

    def backtrack(idx, prev_operand, cur_operand, cur_sum, cur_exp):
        if idx == len(num):
            if cur_operand == 0 and cur_sum == target:
                res.append(cur_exp[1:])
            return
        cur_operand = 10 * cur_operand + int(num[idx])
        if cur_operand > 0:
            backtrack(idx + 1, prev_operand, cur_operand, cur_sum, cur_exp)
        backtrack(idx + 1, cur_operand, 0, cur_sum + cur_operand, cur_exp + '+' + str(cur_operand))
        if cur_exp:
            backtrack(idx + 1, -cur_operand, 0, cur_sum - cur_operand, cur_exp + '-' + str(cur_operand))
            backtrack(idx + 1, prev_operand * cur_operand, 0, cur_sum - prev_operand + prev_operand * cur_operand, cur_exp + '*' + str(cur_operand))
    backtrack(0, 0, 0, 0, '')
    return res
