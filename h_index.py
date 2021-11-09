# LC 274: Calculating h-index
def h_index(citations):
    citations.sort()
    count = 0
    while citations and count < citations[-1]:
        count += 1
        citations.pop()
    return count

