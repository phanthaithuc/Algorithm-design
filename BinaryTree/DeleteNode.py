import collections
from Traversal import TreeTraversal


class Node(TreeTraversal):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        super(Node, self).__init__()


def deleteNode(root: Node, value):
    if root is None:
        print("Node not found")
        return root

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


def inOrder(root: Node):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)



if __name__ == "__main__":
    tree = Node(12)
    tree.left = Node(5)
    tree.left.left = Node(3)
    tree.left.left.left = Node(1)
    tree.right = Node(15)
    tree.right.left = Node(13)
    tree.right.right = Node(17)
    tree.right.right.right = Node(19)
    #deleteNode(tree, 19)
    inOrder(tree)
    # tree_1 = Node(56, Node(30, Node(22, Node(11, Node(3), Node(16)), Node(40))), Node(70, Node(60, Node(65, Node(63), Node(67))), Node(95)))
    tree.print_tree(tree)
