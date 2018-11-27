class TreeNode(object):
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Tree->{val}'.format(val=self.val)

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def serialize(tree_node):
    serialized_tree = []
    depth_first_search(tree_node, serialized_tree)

    return serialized_tree


def depth_first_search(tree_node, serialized_tree):
    if tree_node:
        serialized_tree.append(tree_node.val)
        depth_first_search(tree_node.left, serialized_tree)
        depth_first_search(tree_node.right, serialized_tree)
    else:
        serialized_tree.append(None)


def deserialize(serialized_tree):
    reversed_serialized_tree = list(reversed(serialized_tree))
    root = TreeNode(reversed_serialized_tree.pop())
    _deserialize(reversed_serialized_tree, root)
    return root


def _deserialize(serialized_tree, root):
    if not serialized_tree:
        return

    left = serialized_tree.pop()
    if left:
        root.left = TreeNode(left)
        _deserialize(serialized_tree, root.left)

    right = serialized_tree.pop()
    if right:
        root.right = TreeNode(right)
        _deserialize(serialized_tree, root.right)


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
    print(serialized_tree)
    root_ = deserialize(serialized_tree)
    test_tree1_deserialization(root_)
    assert serialize(root_) == serialize(root)

    root = construct_tree2()
    serialized_tree = serialize(root)
    print(serialized_tree)
    root_ = deserialize(serialized_tree)
    test_tree2_deserialization(root_)
    assert serialize(root_) == serialize(root)
