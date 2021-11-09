# LC 408: word abbreviation
def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
    i = 0
    digit = ''
    abbr_expand = []
    for c in abbr:
        if c.isalpha() and not digit:
            abbr_expand.append(c)
        elif c.isalpha() and digit:
            abbr_expand.extend([digit, c])
            digit = ''
        elif c.isalpha():
            if c == '0' and not digit:
                return False
            digit += c
    if digit:
        abbr_expand.append(digit)
    res = ''
    for c in abbr_expand:
        if c.isalpha():
            res += c
            i += 1
        elif c.isdigit():
            if i + int(c) > len(word):
                return False
            res += word[i:i+int(c)]
            i += int(c)
    return res == word


def word_abbreviation_ii(word, abbr):
    p1 = p2 = 0
    while p1 < len(word) and p2 < len(abbr):
        if abbr[p2].isdigit():
            if abbr[p2] == '0':  # leading zeros are invalid
                return False
            shift = 0
            while p2 < len(abbr) and abbr[p2].isdigit():
                shift = (shift * 10) + int(abbr[p2])
                p2 += 1
            p1 += shift
        else:
            if word[p1] != abbr[p2]:
                return False
            p1 += 1
            p2 += 1
    return p1 == len(word) and p2 == len(abbr)

