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

def preOrder(root : TreeNode):
    if root == None:
        return 0
    print(root.value)
    preOrder(root.left)
    preOrder(root.right)


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

    preOrder(a)