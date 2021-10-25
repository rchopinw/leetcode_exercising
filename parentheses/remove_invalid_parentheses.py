from collections import defaultdict


# LC 301: Remove invalid parentheses
def remove_invalid_parentheses(s):
    rec = defaultdict(set)

    def backtrack(cur, idx, left, right):
        if idx == len(s):
            if left == right:
                rec[len(cur)].add(cur)
            return
        c = s[idx]

        if c.isalpha():
            backtrack(cur + c, idx + 1, left, right)
            return

        backtrack(cur, idx + 1, left, right)

        if c == '(':
            backtrack(cur + c, idx + 1, left + 1, right)
        elif left > right:
            backtrack(cur + c, idx + 1, left, right + 1)

    backtrack('', 0, 0, 0)

    return rec[max(rec)]