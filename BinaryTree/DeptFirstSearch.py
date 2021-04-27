import collections


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#          a
#       /    \
#     b        c
#   /   \       \
# d      e        f

def preOrder(root: TreeNode):
    res = []

    def travel(root):
        if not root:
            return 0
        res.append(root.value)
        preOrder(root.left)
        preOrder(root.right)

    travel(root)

    return res


if __name__ == "__main__":
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(preOrder(a))
