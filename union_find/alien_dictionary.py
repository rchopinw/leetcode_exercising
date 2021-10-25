from collections import defaultdict


def alien_dictionary(words):
    adj = {w: [] for word in words for w in word}
    for w1, w2 in zip(words, words[1:]):
        if len(w1) < len(w2):
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                adj[w2].append(w1)
                break
    visited = {}
    result = []

    def visit(v):
        if v in visited:
            return visited[v]
        visited[v] = False
        for nv in adj[v]:
            r = visit(nv)
            if not r:
                return False
        visited[v] = True
        result.append(v)
        return True

    if not all(visit(x) for x in adj):
        return ""

    return ''.join(result)


# LC 953 is alien sorted
def is_alien_sorted(words, order):
    x_to_i = {x: i for i, x in enumerate(order)}
    for i in range(1, len(words)):
        for c1, c2 in zip(words[i-1], words[i]):
            if c1 != c2:
                if x_to_i[c1] > x_to_i[c2]:
                    return False
                break
        else:
            if len(words[i-1]) > len(words[i]):
                return False
    return True


