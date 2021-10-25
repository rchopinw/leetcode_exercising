# LC 986: Interval Intersection
def interval_intersection(first_list, second_list):
    if not first_list or not second_list:
        return []
    i, j = 0, 0
    results = []
    while i < len(first_list) and j < len(second_list):
        f, s = sorted([first_list[i], second_list[j]])
        if f[0] <= s[0] <= f[1]:
            results.append([max(f[0], s[0]), min(f[1], s[1])])
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1
    return results
