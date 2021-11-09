# LC 1424: FIND DIAGNOAL ORDER
def find_diagnoal_order(nums):
    res = []
    for r, row in enumerate(nums):
        for c, v in enumerate(row):
            res.append((r + c, -r, v))
    res.sort()
    return [x[2] for x in res]
