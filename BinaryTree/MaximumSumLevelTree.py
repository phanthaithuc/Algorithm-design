from Traversal import TreeNode
from Traversal import TreeTraversal
import collections


def maximum_sum_tree_level(root: TreeNode):
    if not root:
        return
    res = []
    tree = []
    stack = collections.deque()
    stack.append(root)
    while stack:
        row = []
        sum_row = 0
        rowSize = len(stack)
        while rowSize > 0:
            current_node = stack.popleft()
            if current_node.left is not None:
                stack.append(current_node.left)
            if current_node.right is not None:
                stack.append(current_node.right)
            rowSize -= 1
            row.append(current_node.val)
            sum_row += current_node.val

        res.append(sum_row)
        tree.append(row)
        level = res.index(max(res))
    return level


if __name__ == "__main__":
    tree2 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                     TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    print(maximum_sum_tree_level(tree2))
    tree1 = TreeNode(1, TreeNode(4, TreeNode(3), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(-1)))
    print(maximum_sum_tree_level(tree1))

    TreeTraversal().print_tree(tree1)
