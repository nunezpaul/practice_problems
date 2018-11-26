class ListNode(object):
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '{val} -> {next}'.format(val=self.val, next=self.next)

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.head)

    def __init__(self, val):
        self.head = ListNode(val)
        self.last = self.head

    def insert(self, val):
        self.last.next = ListNode(val)
        self.last = self.last.next

    def __add__(self, linked_list):
        stack1 = []
        runner1 = self.head
        while runner1:
            stack1.append(runner1.val)
            runner1 = runner1.next

        stack2 = []
        runner2 = linked_list.head
        while runner2:
            stack2.append(runner2.val)
            runner2 = runner2.next

        sum_stack = []
        carry = 0
        while stack1 or stack2:
            num1 = 0
            num2 = 0

            if stack1:
                num1 = stack1.pop()

            if stack2:
                num2 = stack2.pop()

            val = num1 + num2 + carry
            mod_10_val = val % 10
            carry = 0 if val == mod_10_val else 1
            sum_stack.append(mod_10_val)

        if carry > 0:
            sum_stack.append(1)

        sum_linked_list = LinkedList(sum_stack.pop())
        while sum_stack:
            sum_linked_list.insert(sum_stack.pop())

        return sum_linked_list


def generate_linked_lists_1():
    linked_list1 = LinkedList(5)
    linked_list1.insert(6)
    linked_list1.insert(3)

    linked_list2 = LinkedList(8)
    linked_list2.insert(4)
    linked_list2.insert(2)

    answer = LinkedList(1)
    answer.insert(4)
    answer.insert(0)
    answer.insert(5)

    return linked_list1, linked_list2, answer


def generate_linked_lists_2():
    linked_list1 = LinkedList(5)
    linked_list1.insert(6)
    linked_list1.insert(3)

    linked_list2 = LinkedList(8)
    linked_list2.insert(4)

    answer = LinkedList(6)
    answer.insert(4)
    answer.insert(7)

    return linked_list1, linked_list2, answer


def check_linked_lists(sum_linked_list, answer):
    runner1 = sum_linked_list.head
    runner2 = answer.head
    while runner1:
        if runner1.val != runner2.val:
            return False
        runner1 = runner1.next
        runner2 = runner2.next

    return runner1 is None and runner2 is None


if __name__ == '__main__':
    linked_list1, linked_list2, answer = generate_linked_lists_1()
    assert check_linked_lists(linked_list1 + linked_list2, answer)

    linked_list1, linked_list2, answer = generate_linked_lists_2()
    assert check_linked_lists(linked_list1 + linked_list2, answer)

