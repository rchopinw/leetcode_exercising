from collections import deque


# LC 616: Add blod tag in string
def add_blod_tag(s, words):
    windows = set([len(x) for x in words])
    words = set(words)
    tags = []
    for window in windows:
        for i in range(len(s) - window + 1):
            if s[i:i + window] in words:
                tags.append([i, i + window])
    tags.sort()
    if not tags:
        return s
    results = [tags[0]]
    for tag in tags[1:]:
        if tag[1] <= results[-1][1]:
            results[-1][1] = max(results[-1][1], tag[1])
        else:
            results.append(tag)
    results = deque(sum(results, []))
    ans = ''
    open_tag = True
    for i, c in enumerate(s):
        if results and i == results[0]:
            ans += '<b>' if open_tag else '</b>'
            open_tag = not open_tag
            results.popleft()
        ans += c
    return ans + '</b>' if results else ans


