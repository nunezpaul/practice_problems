# Print Binary tree vertically
class TreeNode(object):
    def __repr__(self):
        return 'TreeNode {val}'.format(val=self.val)

    def __str__(self):
        return self.__repr__()

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class VerticalOrder(object):
    def __init__(self, root):
        self.vertical_order = self.get_vertical_order(root)

    def get_vertical_order(self, root):
        runner = root
        history = set()
        order = dict()
        level = 0
        queue = [(runner, level)]
        min_level = float('inf')
        max_level = float('-inf')

        while len(queue) > 0:
            runner, level = queue.pop(0)
            if runner.val not in history:
                child_nodes = self._get_children(runner, level)
                queue += child_nodes
                history.add(runner.val)
                self._add_node_to_order(runner, level, order)
                min_level, max_level = self._update_min_max_level(level, min_level, max_level)

        answer = []
        for i in range(min_level, max_level + 1):
            answer.append(order[i])

        return answer

    def _get_children(self, runner, level):
        left = (runner.left, level - 1)
        right = (runner.right, level + 1)

        valid_nodes = []
        for node, level in (left, right):
            if node:
                valid_nodes.append((node, level))

        return valid_nodes

    def _add_node_to_order(self, runner, level, order):
        if level not in order:
            order[level] = []
        order[level].append(runner.val)

    def _update_min_max_level(self, level, min_level, max_level):
        min_level = min(level, min_level)
        max_level = max(level, max_level)
        return min_level, max_level

def test():
    root = TreeNode(1)
    runner = root

    runner.left = TreeNode(2)
    runner = runner.left

    runner.left = TreeNode(4)
    runner.right = TreeNode(5)

    runner = root
    runner.right = TreeNode(3)
    runner = runner.right

    runner.left = TreeNode(6)
    runner.right = TreeNode(7)
    runner.right.right = TreeNode(9)
    runner.left.right = TreeNode(8)

    assert root.val == 1
    assert root.left.val == 2 and root.right.val ==3
    assert root.left.left.val == 4 and root.left.right.val == 5
    assert root.right.left.val == 6 and root.right.right.val == 7
    assert root.right.left.right.val == 8 and root.right.right.right.val == 9

    return root

if __name__ == '__main__':
    root = test()
    vo = VerticalOrder(root)
    for level in vo.vertical_order:
        print(level)