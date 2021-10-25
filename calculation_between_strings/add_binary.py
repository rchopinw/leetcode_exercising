# LC 67 add binary
def add_binary(a, b):
    a, b, add, r = list(a), list(b), 0, []
    while a and b:
        s = int(a.pop()) + int(b.pop()) + add
        if s >= 2:
            add = 1
            r.append(s % 2)
        else:
            add = 0
            r.append(s)
    while a:
        s = int(a.pop()) + add
        if s >= 2:
            add = 1
            r.append(s % 2)
        else:
            add = 0
            r.append(s)
    while b:
        s = int(b.pop()) + add
        if s >= 2:
            add = 1
            r.append(s % 2)
        else:
            add = 0
            r.append(s)
    if add:
        r.append(add)
    return ''.join(str(x) for x in r[::-1])