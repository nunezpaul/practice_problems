class TreeNode(object):
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "TreeNode -> {val}".format(val=self.val)

    def __init__(self, val):
        self.val = val
        self.children = []


def serialize(root):
    serialized_tree = []
    _depth_first_search(root, serialized_tree)
    return serialized_tree


def _depth_first_search(root, serialized_tree):
    serialized_tree.append(root.val)
    for child in root.children:
        _depth_first_search(child, serialized_tree)
    serialized_tree.append('/')


def deserialize(serialized_tree):
    serialized_tree_copy = list(serialized_tree)
    serialized_tree_copy.reverse()
    root = TreeNode(serialized_tree_copy.pop())
    _deserizlize(root, serialized_tree_copy)
    return root


def _deserizlize(root, serialized_tree):
    val = serialized_tree.pop()
    if val == '/':
        return

    root.children.append(TreeNode(val))
    _deserizlize(root.children[-1], serialized_tree)
    _deserizlize(root, serialized_tree)


def construct_tree1():
    root = TreeNode(1)
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(3))
    root.children.append(TreeNode(4))
    root.children[0].children.append(TreeNode(5))
    root.children[0].children.append(TreeNode(6))
    root.children[0].children.append(TreeNode(7))
    root.children[1].children.append(TreeNode(8))
    root.children[1].children.append(TreeNode(9))
    root.children[2].children.append(TreeNode(10))

    return root


def construct_tree2():
    root = TreeNode(1)
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(3))
    root.children.append(TreeNode(4))
    root.children[0].children.append(TreeNode(5))
    root.children[0].children.append(TreeNode(6))
    root.children[0].children[0].children.append(TreeNode(11))
    root.children[2].children.append(TreeNode(7))
    root.children[2].children.append(TreeNode(8))
    root.children[2].children.append(TreeNode(9))
    root.children[2].children.append(TreeNode(10))

    return root


if __name__ == '__main__':
    root = construct_tree1()
    serialized_tree = serialize(root)
    root_ = deserialize(serialized_tree)
    serialized_tree_ = serialize(root_)
    assert serialized_tree == serialized_tree_

    root = construct_tree2()
    serialized_tree = serialize(root)
    root_ = deserialize(serialized_tree)
    serialized_tree_ = serialize(root_)
    assert serialized_tree == serialized_tree_
