def word_break(s, word_dict):
    memo = {}
    result = dfs(s, set(word_dict), memo)
    return result


def dfs(s, word_dict, memo):
    if s in memo:
        return memo[s]

    if len(s) < 1:
        return []

    result = []
    for word in word_dict:
        has_word = s.startswith(word)
        if not has_word:
            continue
        elif len(s) == len(word):
            result.append(word)
        else:
            possibilities = dfs(s[len(word):], word_dict, memo)
            for possibility in possibilities:
                result.append(word + ' ' + possibility)
    memo[s] = result
    return result



if __name__ == '__main__':
    s = "pineapplepenapple"
    word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(word_break(s, word_dict))

    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    # print(*word_break(s, word_dict))
