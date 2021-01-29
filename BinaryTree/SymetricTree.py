import collections


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isMirror(tree1: Node, tree2: Node):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False

    return tree1.val == tree2.val and isMirror(tree1.right, tree2.left) and isMirror(tree1.left, tree2.right)


def isMirror2(tree1: Node, tree2: Node):
    res = collections.deque()
    res.append(tree1)
    res.append(tree2)
    while res:
        t1 = res.pop()
        t2 = res.pop()
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        res.append(t1.left)
        res.append(t2.right)
        res.append(t1.right)
        res.append(t2.left)
    return True


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(3), Node(4, Node(2))), Node(2, Node(4), Node(3)))
    print(isMirror(tree, tree))
    print(isMirror2(tree, tree))
