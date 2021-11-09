class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        p = 0
        cur = self.tree
        while p < len(word):
            if word[p] in cur:
                if p == len(word) - 1:
                    cur[word[p]][1] = 1
            else:
                cur[word[p]] = [{}, 1] if p == len(word) - 1 else [{}, 0]
            cur = cur[word[p]][0]
            p += 1

    def search(self, word: str) -> bool:
        cur, flag = self.tree, 0
        for c in word:
            if c in cur:
                cur, flag = cur[c]
            else:
                return False
        return flag == 1

    def startsWith(self, prefix: str) -> bool:
        cur = self.tree
        for c in prefix:
            if c in cur:
                cur = cur[c][0]
            else:
                return False
        return True
