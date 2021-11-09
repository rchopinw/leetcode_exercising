# LC 970 Powerful integers
import math


def powerful_integers(x, y, bound):
    if x == y == 1:
        return [2] if bound > 1 else []
    if bound <= 1:
        return []
    if x == 1 or y == 1:
        t = x if x != 1 else y
        return [t**i + 1 for i in range(int(math.log(bound, t)) + 1) if t**i + 1 <= bound]
    res = set()
    a = int(math.log(bound, x)) + 1
    b = int(math.log(bound, y)) + 1
    for i in range(a):
        for j in range(b):
            val = x**i + y**j
            if val <= bound:
                res.add(val)
    return res
