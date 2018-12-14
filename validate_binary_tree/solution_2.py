class TreeNode(object):
    def __str__(self):
        left = self.left.val if self.left else 'N'
        right = self.right.val if self.right else 'N'
        return "{left} {val} {right}".format(val=self.val, left=left, right=right)

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None



def is_valid_tree(root):
    flattened_tree = []
    _traverse_tree(root, flattened_tree)
    return _is_in_order(flattened_tree)


def _traverse_tree(root, flattened_tree):
    if root:
        _traverse_tree(root.left, flattened_tree)
        flattened_tree.append(root.val)
        _traverse_tree(root.right, flattened_tree)

    return


def _is_in_order(flattened_tree):
    for idx, num in enumerate(flattened_tree):
        if idx == 0:
            prev_num = num
            continue

        if prev_num > num:
            return False
        prev_num = num

    return True


def construct_bad_tree():
    root = TreeNode(4)

    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    root.right = TreeNode(10)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(12)
    root.right.left.left = TreeNode(5)
    root.right.left.right = TreeNode(8)
    root.right.right.right = TreeNode(14)
    root.right.right.left = TreeNode(11)

    return root


def construct_good_tree():
    root = TreeNode(4)

    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    # root.left.right = TreeNode(2)

    root.right = TreeNode(10)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(12)
    root.right.left.left = TreeNode(5)
    root.right.left.right = TreeNode(8)
    root.right.right.right = TreeNode(14)
    root.right.right.left = TreeNode(11)

    return root


def construct_bad_tree2():
    root = TreeNode(5)

    root.left = TreeNode(1)

    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    return root


def construct_good_tree2():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)


if __name__ == '__main__':
    bad_root = construct_bad_tree()
    assert not is_valid_tree(bad_root)

    good_root = construct_good_tree()
    assert is_valid_tree(good_root)

    bad_root2 = construct_bad_tree2()
    assert not is_valid_tree(bad_root2)

    good_root2 = construct_good_tree2()
    assert is_valid_tree(good_root2)