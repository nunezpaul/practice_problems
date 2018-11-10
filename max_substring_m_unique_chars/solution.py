class StringQueue(object):
    def __init__(self, unique_char_limit):
        self.unique_char_limit = unique_char_limit
        self.string = []
        self.char_count = {}
        self.num_uniques = 0
        self.start = 0
        self.end = 0
        self.max_len = 0

    def add_char(self, char):
        seen_before = char in self.char_count
        can_add_unique = self.num_uniques + 1 <= self.unique_char_limit

        if seen_before:
            self._add_char(char)
        elif can_add_unique:
            self._add_char(char)
            self.num_uniques += 1
        else:
            self._remove_unique_char()
            self.add_char(char)

        self.end += 1
        self.max_len = max(self.max_len, self.end - self.start)


    def _add_char(self, char):
        self.string.append(char)
        self.char_count[char] = self.char_count.get(char, 0) + 1

    def _remove_unique_char(self):
        while True:
            char = self.string[self.start]

            self.char_count[char] -=1
            self.start += 1
            if self.char_count[char] == 0:
                break
        self.char_count.pop(char)
        self.num_uniques -= 1



def find_max_substring(chars, unique_char_limit):
    string_queue = StringQueue(unique_char_limit)

    for char in chars:
        string_queue.add_char(char)

    return string_queue.max_len

if __name__ == '__main__':
    chars = 'aaaaaababcbaaabbdef'
    print(find_max_substring(chars, unique_char_limit=3))

    chars = ''
    print(find_max_substring(chars, unique_char_limit=2))