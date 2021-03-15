from isBinaryTree import Node
from Traversal import TreeTraversal
import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.parent = None
        self.val = val


def lca(root: TreeNode, x: TreeNode, y: TreeNode) -> TreeNode:
    if not root:
        return
    if root.val == x.val or root.val == y.val:
        return root

    left_search = lca(root.left, x, y)
    right_search = lca(root.right, x, y)
    if left_search is not None and right_search is not None:
        return root
    if left_search is None and right_search is None:
        return None

    return left_search if left_search else right_search


def tree_height(root: TreeNode) -> int:
    if not root:
        return -1

    left_height = tree_height(root.left) + 1
    right_height = tree_height(root.right) + 1

    return max(right_height, left_height)


def isSymmetric(root: TreeNode) -> bool:
    return helper(root, root)


def helper(root1: TreeNode, root2: TreeNode) -> bool:
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.val == root2.val and helper(root1.left, root2.right) and helper(root1.right, root2.left)


def revert_binary(root: TreeNode) -> TreeNode:
    if not root:
        return
    temp = root.left
    root.left = root.right
    root.right = temp

    revert_binary(root.left)
    revert_binary(root.right)
    return root


def right_view(root: TreeNode):
    if not root:
        return
    res = []
    stack = collections.deque()
    stack.append(root)
    while stack:
        row = []
        rowSize = len(stack)
        while rowSize > 0:
            current_node = stack.popleft()
            if current_node.left is not None:
                stack.append(current_node.left)
            if current_node.right is not None:
                stack.append(current_node.right)
            row.append(current_node.val)
            rowSize -= 1
        res.append(row[-1])

    return res


def zigzag_travelsal(root: TreeNode) -> None:
    if not root:
        return

    stack = collections.deque()
    stack.append(root)
    res = []
    result = []
    count = -1

    while stack:
        rowSize = len(stack)
        row = []
        while rowSize > 0:
            current_node = stack.popleft()
            if current_node.left is not None:
                stack.append(current_node.left)
            if current_node.right is not None:
                stack.append(current_node.right)

            row.append(current_node.val)
            rowSize -= 1
            result.append(row[0])
        count += 1
        if count % 2 == 0:
                res.append([count,row])
        elif count % 2 != 0:
            res.append([count, row[::-1]])
    print("Tree level:", count, "level")
    return res


if __name__ == "__main__":
    # root = TreeNode('a')
    # root.left = TreeNode('b')
    # root.left.parent = root
    # root.right = TreeNode('c')
    # root.right.parent = root
    # a = root.right.left = TreeNode('d')
    # root.right.left.parent = root.right
    # b = root.right.right = TreeNode('e')
    # root.right.right.parent = root.right
    #
    # res = lowest_common_ancestor(root, TreeNode('b'), TreeNode('e'))
    # print(res.val)

    tree = TreeNode('a')
    tree.left = TreeNode('b')
    tree.right = TreeNode('c')
    tree.left.left = TreeNode('f')
    tree.right.left = TreeNode('d')
    tree.right.right = TreeNode('e')
    tree.right.right.right = TreeNode('l')
    tree.right.right.left = TreeNode('m')
    tree.right.right.right.right = TreeNode('n')
    tree.right.right.right.left = TreeNode('o')

    result = lca(tree, TreeNode('f'), TreeNode('m'))
    print(result.val)
    print(tree_height(tree))

    root = TreeNode(1, TreeNode(5, TreeNode(7), TreeNode(6)), TreeNode(8, TreeNode(9), TreeNode(10)))
    root_revert = revert_binary(root)

    TreeTraversal().print_tree(root)

    print("Right view: ", right_view(root))

    TreeTraversal().print_tree(tree)
    print(zigzag_travelsal(tree))
