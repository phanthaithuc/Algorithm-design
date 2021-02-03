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


def inOrderIntersive(treenode: Node):
    queue = []
    queue.append(treenode)
    res = []
    while queue:
        current_node = queue.pop()
        if current_node.left is not None:
            queue.append(current_node.left)
            res.append(current_node.val)
        if current_node.right is not None:
            queue.append(current_node.right)

    return res


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


def search(root: Node, value):
    if root is None:
        print("Not Found", value)
        return -1

    if value == root.val:
        print("Founded", value)
        return 1
    elif value > root.val:
        return search(root.right, value)
    elif value < root.val:
        return search(root.left, value)


def inOrderRecursive(root: Node):
    if root is None:
        return
    inOrderRecursive(root.left)
    print(root.val)
    inOrderRecursive(root.right)


def deleteNode(root: Node, value):
    if root is None:
        print("Node not found")
        return -1

    if root.val == value:

        # Node has right child or left child:
        if not root.right or not root.left:
            root = root.left if root.left else root.right

        # Node node has both right and left child:
        else:
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = deleteNode(root.right, curr.val)

    elif value > root.val:
        root.right = deleteNode(root.right, value)
    elif value < root.val:
        root.left = deleteNode(root.left, value)

    return root


#      7
#    /   \
#   4     9
#  / \   /  \
# 1   6 8    15
# /          /  \
# 0         11   17
if __name__ == "__main__":
    tree = Node(7, Node(4, Node(1, Node(0), Node(2)), Node(6)), Node(9, Node(8), Node(15, Node(11), Node(17))))
    tree_dup = Node(1, Node(1))
    # print(isBST(tree))
    # print(recursive(tree))
    #
    # print(isBST(tree_dup))
    inOrderRecursive(tree)
    deleteNode(tree, 555)
    inOrderRecursive(tree)


