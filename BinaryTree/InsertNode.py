class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertNode(root: Node, value):
    if not root:
        return Node(value)
    if value > root.val:
        root.right = insertNode(root.right, value)
    if value < root.val:
        root.left = insertNode(root.left, value)
    return root


def insertNodeIntensive(root: Node, value):
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


def printnode(root: Node, level = 0):
    if not root:
        return
    printnode(root.right, level + 1)
    print("  " * 4 * level + ' |--> ', root.val)
    printnode(root.left, level + 1)


#      7
#    /   \
#   4     9
#  / \   /  \
# 1   6 8    15
# / \         /  \
# 0  2       11   17

if __name__ == "__main__":
    tree = Node(7, Node(4, Node(1, Node(0), Node(2)), Node(6)), Node(9, Node(8), Node(15, Node(11), Node(17))))
    insertNodeIntensive(tree, 5)
    printnode(tree)

