from collections import deque, defaultdict


# LC 127: Word Ladder
def word_ladder(begin, end, word_list):
    """
    Time Complexity: O(M^2 * N), where M is the length of each word and N is the total number of words
                     in the input word list. For each word in the word list, we iterate over its length to
                     find all the intermediate words corresponding to it. Since the length of each word
                     is MM and we have NN words, the total number of iterations the algorithm takes to
                     create patterns is M \times NM×N. Additionally, forming each of the intermediate
                     word takes O(M)O(M) time because of the substring operation used to create the new string.
                     This adds up to a complexity of O(M^2 x N).
                     The BFS part in the worst case might take up to N words. For each word, we will examine M possible
                     outcomes, because we used the string operation to generate all the substrings, it takes in all
                     O(M^2) time.
    Space Complexity: O(M^2 * N)
    :param begin:
    :param end:
    :param word_list:
    :return:
    """
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

