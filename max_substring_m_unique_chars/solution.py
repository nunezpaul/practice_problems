class DoublyLinkedList(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def insert_next(self, val):
        next = DoublyLinkedList(val)
        self.next = next
        next.prev = self

    def insert_prev(self, val):
        prev = DoublyLinkedList(val)
        self.prev = prev
        prev.next = self



class LinkedHashMap(object):
    def __init__(self):
        self.linked_list = DoublyLinkedList('start')
        self.linked_list.insert_next('end')
        self.shortcut_maps = {'start': self.linked_list, 'end': self.linked_list.next}

    def push(self, val):
        end = self.shortcut_maps['end']
        prev_last = end.prev
        new_last = DoublyLinkedList(val)

        prev_last.next = new_last
        new_last.prev = prev_last
        end.prev = new_last
        new_last.next = end

        self.shortcut_maps[val] = new_last

    def pop(self, val=None):
        old_first = self.shortcut_maps[val] if val else self.shortcut_maps['start'].next
        new_first = old_first.next  # previously second in the list
        start = old_first.prev

        start.next = new_first
        new_first.prev = start

        self.shortcut_maps.pop(old_first.val)

        return old_first.val

    def contains(self, val):
        return val in self.shortcut_maps

    def get_list(self):
        runner = self.shortcut_maps['start']
        result = [runner.val]
        while runner.next:
            result.append(runner.next.val)
            runner = runner.next
        return result


class StringQueue(object):
    def __init__(self, unique_char_limit):
        self.max_allowable_unique_chars = unique_char_limit
        self.last_char_idx = {}
        self.linked_hashmap = LinkedHashMap()
        self.max_length = 0
        self.start_idx = 0
        self.curr_idx = 1
        self.num_unique_chars = 0

    def add_char(self, char):
        char_seen_before = self.linked_hashmap.contains(char)
        can_add_another_unique = self.num_unique_chars + 1 <= self.max_allowable_unique_chars
        self.last_char_idx[char] = self.curr_idx


        if char_seen_before:
            self.linked_hashmap.pop(char)
            self.linked_hashmap.push(char)
        elif can_add_another_unique:
            self.linked_hashmap.push(char)
            self.num_unique_chars += 1
        else:
            prev_char = self.linked_hashmap.pop()
            self.linked_hashmap.push(char)
            self.start_idx = self.last_char_idx[prev_char]
            self.last_char_idx.pop(prev_char)

        self.max_length = max(self.max_length, self.curr_idx - self.start_idx)
        self.curr_idx += 1


def find_max_substring(chars, unique_char_limit):
    string_queue = StringQueue(unique_char_limit)

    for char in chars:
        string_queue.add_char(char)
        string_queue.linked_hashmap.get_list()

    return string_queue.max_length

def linked_hashmap_test():
    linked_hashmap = LinkedHashMap()
    linked_hashmap.push('a')
    linked_hashmap.push('b')
    linked_hashmap.push('c')
    linked_hashmap.push('d')
    linked_hashmap.push('e')

    assert (['start', 'a', 'b', 'c', 'd', 'e', 'end'] == linked_hashmap.get_list())

    assert 'c' == linked_hashmap.pop('c')
    assert ['start', 'a', 'b', 'd', 'e', 'end'] == linked_hashmap.get_list()

    assert 'a' == linked_hashmap.pop()
    assert ['start', 'b', 'd', 'e', 'end'] == linked_hashmap.get_list()

    assert 'b' == linked_hashmap.pop()
    assert ['start', 'd', 'e', 'end'] == linked_hashmap.get_list()

    assert 'e' == linked_hashmap.pop('e')
    assert ['start', 'd', 'end'] == linked_hashmap.get_list()

    assert ['start', 'd', 'end'] == linked_hashmap.get_list()
    print('Test passed!')

if __name__ == '__main__':
    chars = 'aababcbaaabbdef'
    for i in range(1, 8):
        result = find_max_substring(chars, unique_char_limit=i)
        print('Longest substring for {i} unique chars is {result}'.format(i=i, result=result))
        print('----------')

    chars = ''
    result = find_max_substring(chars, unique_char_limit=2)
    print('Longest substring for {i} unique chars is {result}'.format(i=2, result=result))
