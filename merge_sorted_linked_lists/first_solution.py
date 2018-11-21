class ListNode(object):
    def __str__(self):
        return 'LinkedList -> {}'.format(self.val)

    def __repr__(self):
        return self.__str__()

    def __init__(self, val):
        self.val = val
        self.next = None


def merge_k_linked_lists(linked_lists):
    inspect_linked_lists(linked_lists)
    min_idx = find_min_node(linked_lists)
    head = pop_head_node(linked_lists, min_idx)
    runner = head

    while linked_lists:
        min_idx = find_min_node(linked_lists)
        next = pop_head_node(linked_lists, min_idx)
        runner.next = next
        runner = runner.next

    return head


def find_min_node(linked_lists):
    min_val = float('inf')
    for idx, linked_list in enumerate(linked_lists):
        if linked_list.val < min_val:
            min_val = linked_list.val
            min_idx = idx

    return min_idx


def pop_head_node(linked_lists, idx_to_pop):
    head = linked_lists[idx_to_pop]
    next = head.next
    head.next = None
    if next:
        linked_lists[idx_to_pop] = next
    else:
        linked_lists.pop(idx_to_pop)

    return head


def test():
    linked_lists = []
    for array in ([1, 4, 5], [1, 3, 4], [2, 6]):
        linked_lists.append(convert_to_linked_list(array))

    return merge_k_linked_lists(linked_lists)


def convert_to_linked_list(array):
    for idx, element in enumerate(array):
        if idx == 0:
            head = ListNode(element)
            runner = head
            continue

        runner.next = ListNode(element)
        runner = runner.next
    return head


def inspect_linked_lists(linked_lists):
    heads = list(linked_lists)
    for head in heads:
        inspect_linked_list(head)


def inspect_linked_list(head):
    result = []
    runner = head
    while runner:
        result.append(str(runner.val))
        runner = runner.next
    print(" -> ".join(result))


if __name__ == '__main__':
    result = test()
    inspect_linked_list(result)