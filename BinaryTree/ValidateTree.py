class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def ValidateTree(tree: Node):
    traversal = []

    def inOrder(root: Node):
        stack = []
        stack.append(root)
        if root.left is not None:
            stack.append(root.left)
        if root.left is not None:
            stack.append(root.right)


    inOrder(tree)

    if len(traversal) != len(set(traversal)):
        return False
    else:
        return traversal == sorted(traversal)



if __name__ == "__main__":
    tree = Node(5, Node(1), Node(4, Node(3), Node(6)))
    print(ValidateTree(tree))