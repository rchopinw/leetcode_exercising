from collections import defaultdict


# LC 249: Group shifted strings
def convert(s):
    if len(s) == 1:
        return 0
    return tuple(ord(s[i]) - ord(s[i-1]) + 26 if ord(s[i]) - ord(s[i-1]) < 0 else ord(s[i]) - ord(s[i-1]) for i in range(1, len(s)))


def group_strings(strings):
    rec = defaultdict(list)
    for string in strings:
        rec[convert(string)].append(string)
    return rec.values
