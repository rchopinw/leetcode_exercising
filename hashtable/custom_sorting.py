from collections import Counter


# LC 791 Custom sorting
def custom_sorting_string(order, s):
    x_to_i = {x: i for i, x in enumerate(order)}
    s_out = ''.join(c for c in s if c in x_to_i)
    res = []
    for c in s:
        if c in x_to_i:
            if not res:
                res.append(c)
            else:
                for i, item in enumerate(res):
                    if x_to_i[item] >= x_to_i[c]:
                        res.insert(i, c)
                        break
                else:
                    res.append(c)
    return ''.join(res) + s_out


def custom_sorting_string_ii(order, s):
    """
    Linear time solution: O(T + S)
    Space complexity: O(T)
    :param order:
    :param s:
    :return:
    """
    count = Counter(s)
    ans = ''
    for c in order:
        ans += c * count[c]
        count[c] = 0
    for c in s:
        ans += c * count[c]
    return ans
