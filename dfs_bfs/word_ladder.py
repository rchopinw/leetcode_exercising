from collections import deque, defaultdict


# LC 127: Word Ladder
def word_ladder(begin, end, word_list):
    word_list.append(begin)
    patterns = defaultdict(set)
    for word in word_list:
        for i, c in enumerate(word):
            patterns[word[:i] + '*' + word[i+1:]].add(word)
    queue = deque([(begin, 1)])
    visited = set()
    while queue:
        w, d = queue.popleft()
        for pattern in [w[:i] + '*' + w[i+1:] for i in range(len(w))]:
            for nxt in patterns[pattern]:
                if nxt == end:
                    return d + 1
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, d + 1))
    return 0

