import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inOrder(root: Node):
    current_node = root
    stack = collections.deque()
    stack.append(current_node)

    while stack:
        if current_node.left is not None:
            stack.append(current_node.left)


if __name__ == "__main__":
    tree = Node(12)
    tree.left = Node(5)
    tree.left.left = Node(3)
    tree.left.left.left = Node(1)
    tree.right = Node(15)
    tree.right.left = Node(13)
    tree.right.right = Node(17)
    tree.right.right.right = Node(19)
