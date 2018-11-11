import collections

class StringQueue(object):
    def __init__(self, unique_char_limit):
        self.max_allowable_unique_chars = unique_char_limit
        self.linked_hashmap = collections.OrderedDict()
        self.max_length = 0
        self.start_idx = 0
        self.curr_idx = 1
        self.num_unique_chars = 0

    def add_char(self, char):
        char_seen_before = char in self.linked_hashmap
        can_add_another_unique = self.num_unique_chars + 1 <= self.max_allowable_unique_chars

        if char_seen_before:
            self.linked_hashmap.pop(char)
            self.linked_hashmap[char] = self.curr_idx
        elif can_add_another_unique:
            self.linked_hashmap[char] = self.curr_idx
            self.num_unique_chars += 1
        else:
            prev_char, self.start_idx = self.linked_hashmap.popitem(last=False)
            self.linked_hashmap[char] = self.curr_idx

        self.max_length = max(self.max_length, self.curr_idx - self.start_idx)
        self.curr_idx += 1


def find_max_substring(chars, unique_char_limit):
    string_queue = StringQueue(unique_char_limit)

    for char in chars:
        string_queue.add_char(char)

    return string_queue.max_length

if __name__ == '__main__':
    chars = 'aababcbaaabbdef'
    for i in range(1, 8):
        result = find_max_substring(chars, unique_char_limit=i)
        print('Longest substring for {i} unique chars is {result}'.format(i=i, result=result))
        print('----------')

    chars = ''
    result = find_max_substring(chars, unique_char_limit=2)
    print('Longest substring for {i} unique chars is {result}'.format(i=2, result=result))
