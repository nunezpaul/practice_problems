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
    return _is_valid_tree(root, root)


def _is_valid_tree(branch, root, result=True):
    if branch is None:
        return result
    result = validate_node(branch.val, root)
    # print(branch.val, result)
    if result:
        left =_is_valid_tree(branch.left, root, result)
        right = _is_valid_tree(branch.right, root, result)
        return left and right

    return False


def validate_node(val, root):
    print(val, '//', root)
    if root is None:
        return False
    if root.val == val:
        return True
    elif val < root.val:
        return validate_node(val, root.left)
    else:
        return validate_node(val, root.right)


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


if __name__ == '__main__':
    bad_root = construct_bad_tree()
    print(is_valid_tree(bad_root))

    good_root = construct_good_tree()
    print(is_valid_tree(good_root))