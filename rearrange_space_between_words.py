# lc 1592: rearrange spaces between words
def rearrange_spaces(text):
    words = [x for x in text.split(' ') if x]
    spaces = text.count(' ')
    if len(words) == 1:
        return words[0] + spaces * ' '
    mid = spaces // (len(words) - 1)
    end = spaces % (len(words) - 1)
    return (' ' * mid).join(words) + ' ' * end
