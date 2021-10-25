# LC 139: word break
def word_break(s, word_dict):
    word_dict = set(word_dict)
    dp = [True] + [False for _ in range(len(s))]
    for i in range(len(s) + 1):
        for j in range(i):
            if dp[j] and dp[j:i] in word_dict:
                dp[i] = True
    return dp[-1]


# LC 140: word break ii
def word_break_ii(s, word_dict):
    word_dict = set(word_dict)
    dp = {i: [] for i in range(len(s) + 1)}
    dp[0] = [[]]
    for i in range(len(s) + 1):
        for j in range(i):
            if dp[j] and dp[j:i] in word_dict:
                for combination in dp[j]:
                    dp[i].append(combination + [s[j:i]])
    return [' '.join(x) for x in dp[len(s)]]
