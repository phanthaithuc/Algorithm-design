class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertNode(root: Node, value: int) -> Node:
    if not root:
        return Node(value)
    if value > root.val:
        root.right = insertNode(root.right, value)
    if value < root.val:
        root.left = insertNode(root.left, value)
    return root


def insertNodeIntensive(root: Node, value: int) -> Node:
    if not root:
        return Node(value)
    tree = root
    while tree:
        if value < tree.val:
            if tree.left:
                tree = tree.left
            else:
                tree.left = Node(value)
                break
        if value > tree.val:
            if tree.right:
                tree = tree.right
            else:
                tree.right = Node(value)
                break

    return root


def preOrder(root: Node):
    if not root:
        return
    preOrder(root.left)
    print(root.val)
    preOrder(root.right)


def printnode(root: Node, level=0):
    if not root:
        return
    printnode(root.right, level + 1)
    print("  " * 4 * level + ' |-->', root.val)
    printnode(root.left, level + 1)


def print_node(root: Node, level=0):
    if not root:
        return
    printnode(root.right)


# Lowest commend ancestor

def lca(root: Node, a: Node, b: Node) -> Node:
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


def lcaII(root: Node, x: Node, y: Node) -> Node:
    if root.val > x.val and root.val > y.val:
        return lcaII(root.left, x, y)
    if root.val < x.val and root.val < y.val:
        return lcaII(root.right, x, y)
    return root


#
# def isBalance(root: Node, level = 0):
#     if not root:
#         return 0
#     leftheight = isBalance(root.left, level + 1)
#     rightheight = isBalance(root.right, level + 1)


def treeheight(root: Node):
    if not root:
        return -1
    return (treeheight(root.left) + 1) >= (treeheight(root.right) + 1)


#      7
#    /   \
#   4     9
#  / \   /  \
# 1   6 8    15
# / \        /  \
# 0  2     11   17

if __name__ == "__main__":
    tree = Node(7, Node(4, Node(1, Node(0), Node(2)), Node(6)), Node(9, Node(8), Node(15, Node(11), Node(17))))
    insertNodeIntensive(tree, 5)
    printnode(tree)
    print(lca(tree, Node(17), Node(8)).val)
    print(lcaII(tree, Node(17), Node(11)).val)
    print(treeheight(tree))
