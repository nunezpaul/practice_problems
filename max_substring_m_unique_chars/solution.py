class StringQueue(object):
    def __init__(self, unique_char_limit):
        self.string = []
        self.last_unique_chars_pos = {}
        self.num_unique_chars = 0
        self.max_allowable_unique_chars = unique_char_limit
        self.length = 0
        self.max_length = 0

    def add_char(self, char):
        check1 = char in self.last_unique_chars_pos
        check2 = self.num_unique_chars + 1 <= self.max_allowable_unique_chars
        if check1 or check2:
            self.num_unique_chars += 1 if not check1 else 0
            self.string.append(char)
            self.length += 1
            self.last_unique_chars_pos[char] = self.length - 1
            self.max_length = max(self.max_length, self.length)
        else:
            self._add_new_unique_char(char)

    def _add_new_unique_char(self, char):
        key_to_remove = self._find_minimum_to_remove()
        reset_val = self.last_unique_chars_pos[key_to_remove] + 1
        self._update_internal_values(key_to_remove, reset_val)
        self.add_char(char)

    def _find_minimum_to_remove(self):
        min_val = float('inf')
        min_key = None
        for key, val in self.last_unique_chars_pos.items():
            if val < min_val:
                min_val = val
                min_key = key
        return min_key

    def _update_internal_values(self, key_to_remove, reset_val):
        for key, val in self.last_unique_chars_pos.items():
            self.last_unique_chars_pos[key] = val - reset_val

        self.string = self.string[reset_val:]
        self.last_unique_chars_pos.pop(key_to_remove)
        self.num_unique_chars -= 1
        self.length -= reset_val

def find_max_substring(chars, unique_char_limit):
    string_queue = StringQueue(unique_char_limit)

    for char in chars:
        string_queue.add_char(char)

    return string_queue.max_length

if __name__ == '__main__':
    chars = 'aaaaaababcbaaabbdef'
    print(find_max_substring(chars, unique_char_limit=3))

    chars = ''
    print(find_max_substring(chars, unique_char_limit=2))