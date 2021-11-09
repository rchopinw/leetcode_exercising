# LC 670 Maximum Swap
def maximum_swap(num):
    mi, m, recs, num = 0, -1, [], list(int(x) for x in str(num))
    for i in range(len(num) - 1, -1, -1):
        if m < num[i]:
            m = num[i]
            mi = i
        recs.append(mi)
    recs.reverse()
    for i, v in enumerate(num):
        if v < num[recs[i]]:
            num[recs[i]], num[i] = num[recs[i]], num[i]
    return int(''.join(str(x) for x in num))
