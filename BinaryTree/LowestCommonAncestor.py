from isBinaryTree import Node


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


#   a
#  / \
# b   c
#    / \
#   d*  e*

def lca(root: TreeNode, a: TreeNode, b: TreeNode) -> TreeNode:
    if not root:
        return
    if root.val == a.val or root.val == b.val:
        return root
    leftSearch = lca(root.left, a, b)
    rightSearch = lca(root.right, a, b)

    if leftSearch is None:
        return rightSearch
    if rightSearch is None:
        return leftSearch
    return root


if __name__ == "__main__":
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.left.parent = root
    root.right = TreeNode('c')
    root.right.parent = root
    a = root.right.left = TreeNode('d')
    root.right.left.parent = root.right
    b = root.right.right = TreeNode('e')
    root.right.right.parent = root.right

    print(lca(root, a, b).val)

    tree = Node("A", Node("B"), Node("C"))
    print(tree)
