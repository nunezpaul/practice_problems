import collections

class TreeNode(object):
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Tree->{val}'.format(val=self.val)

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def serialize(root):
    serialized_tree = []
    prev_level = 0
    queue = collections.deque()
    queue.append((0, root))

    while queue:
        curr_level, curr_node = queue.popleft()

        serialized_val = curr_node.val if curr_node is not None else None
        serialized_tree.append(serialized_val)

        if curr_node is not None:
            queue.append((curr_level + 1, curr_node.left))
            queue.append((curr_level + 1, curr_node.right))

    return serialized_tree


def deserialize(serialized_tree):
    reversed_serialized_tree = list(reversed(serialized_tree))
    root = TreeNode(reversed_serialized_tree.pop())
    queue = collections.deque([root])
    while queue:
        curr_node = queue.popleft()

        left = reversed_serialized_tree.pop()
        if left is not None:
            left_node = TreeNode(left)
            curr_node.left = left_node
            queue.append(left_node)

        right = reversed_serialized_tree.pop()
        if right is not None:
            right_node = TreeNode(right)
            curr_node.right = right_node
            queue.append(right_node)

    return root






def construct_tree1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def test_tree1_deserialization(root_):
    assert root_.val == 1
    assert root_.left.val == 2
    assert root_.right.val == 3
    assert root_.left.left.val == 4
    assert root_.left.right.val == 5
    assert root_.right.left.val == 6
    assert root_.right.right.val == 7


def construct_tree2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    return root


def test_tree2_deserialization(root_):
    assert root_.val == 1
    assert root_.left.val == 2
    assert root_.right.val == 3
    assert root_.right.right.val == 4
    assert root_.right.right.right.val == 5


if __name__ == '__main__':
    root = construct_tree1()
    serialized_tree = serialize(root)
    root_ = deserialize(serialized_tree)
    test_tree1_deserialization(root_)
    assert serialize(root_) == serialize(root)

    root = construct_tree2()
    serialized_tree = serialize(root)
    root_ = deserialize(serialized_tree)
    test_tree2_deserialization(root_)
    assert serialize(root_) == serialize(root)
