from BinaryTree.isBinaryTree import deleteNode
from BinaryTree.isBinaryTree import inOrderRecursive
from BinaryTree.isBinaryTree import Node




# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


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
