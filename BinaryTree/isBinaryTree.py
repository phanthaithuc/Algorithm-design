class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBST(root: Node):
    stack = []

    def inOrder(tree: Node):
        if tree is None:
            return
        inOrder(tree.left)
        stack.append(tree.val)
        inOrder(tree.right)

    inOrder(root)

    if len(stack) != len(set(stack)):
        return False
    else:
        return stack == sorted(stack)


def recursive(root: Node):
    if root is None:
        return True
    if isSmaller(root.left, root.val) and isGreater(root.right, root.val) \
            and recursive(root.left) and recursive(root.right):
        return True
    else:
        return False


def isGreater(root: Node, curr_value):
    if root is None:
        return
    if root.val < curr_value and isGreater(root.right, curr_value) and isGreater(root.left, curr_value):
        return True
    else:
        return False


def isSmaller(root: Node, curr_value):
    if root is None:
        return
    if root.val > curr_value and isSmaller(root.left, curr_value) and isSmaller(root.right, curr_value):
        return True
    else:
        return False


if __name__ == "__main__":
    tree = Node(7, Node(4, Node(1), Node(6)), Node(9))
    tree_dup = Node(1, Node(1))
    print(isBST(tree))

    list = [1, 2, 3, 5, 4]

    print(isBST(tree_dup))

    print(recursive(tree))
