class LongestCommonSubstring(object):
    def __init__(self, s1, s2):
        self.s1 = '$'.join(s1)
        self.s2 = '$'.join(s2)
        self.matrix, self.max_substring_len, self.max_s1_idx = self._construct_maxtrix()

    def _construct_maxtrix(self):
        matrix = []
        max_substring_len = 0
        max_s1_idx = 0
        for y, val1 in enumerate(self.s1):
            row = []
            for x, val2 in enumerate(self.s2):
                are_not_spacer = val1 != '$' and val2 != '$'
                are_equal = val1 == val2
                result = self._get_score(y, x, matrix) if are_not_spacer and are_equal else 0
                if result > max_substring_len:
                    max_substring_len = result
                    max_s1_idx = y
                row.append(result)
            matrix.append(row)

        return matrix, max_substring_len, max_s1_idx

    def _get_score(self, y, x, matrix):
        new_x = x - 1
        new_y = y - 1

        if not (new_x >= 0):
            return 1

        if not (new_y >= 0):
            return 1

        return matrix[new_y][new_x] + 1

    def get_max_substring(self):
        return self.s1[self.max_s1_idx - self.max_substring_len + 1: self.max_s1_idx + 1]


def test():
    s1 = "what happened".split()
    s2 = "happiness".split()
    lcs = LongestCommonSubstring(s1, s2)
    assert 'happ' == lcs.get_max_substring()

    s1 = 'happiness is happy'.split()
    s2 = 'happy feet makes me happy'.split()
    lcs = LongestCommonSubstring(s1, s2)
    assert 'happy' == lcs.get_max_substring()

    s1 = "no more baby don't hurt me".split()
    s2 = "don't hurt me no more".split()
    lcs = LongestCommonSubstring(s1, s2)
    assert "don't" == lcs.get_max_substring()


if __name__ == '__main__':
    s1 = "given an array of words find what is and how long is the  length of".split()
    s2 = "find what is length of the longest common substring between two words in the array".split()
    test()
    lcs = LongestCommonSubstring(s1, s2)
    print(lcs.get_max_substring())

