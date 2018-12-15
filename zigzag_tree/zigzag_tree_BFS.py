import collections

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return "{left} {val} {right}".format(left=left, val=self.val, right=right)


def zigzag_tree(root):
    levels = DFS_traverse(root)
    zig_zagged_levels = zig_zag(levels)
    return zig_zagged_levels


def zig_zag(levels):
    level = 0
    while level in levels:
        if level % 2 == 1:
            levels[level] = list(reversed(levels[level]))
        level += 1
    result = [val for key, val in levels.items()]
    return result


def DFS_traverse(root):
    levels = {}
    queue = collections.deque()
    curr_level = 0
    if root is not None:
        queue.append((root, curr_level))

    while queue:
        curr_node, curr_level = queue.popleft()
        if curr_level not in levels:
            levels[curr_level] = []
        levels[curr_level].append(curr_node.val)

        queue += [(curr_node.left, curr_level + 1)] if curr_node.left else []
        queue += [(curr_node.right, curr_level + 1)] if curr_node.right else []
    return levels


def construct_tree():
    root = TreeNode(3)

    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.righ = TreeNode(7)

    return root

if __name__ == '__main__':
    root = construct_tree()
    print(zigzag_tree(root))