import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeTraversal:

    def InOrder(self, root: TreeNode):
        if root is None:
            return
        self.InOrder(root.left)
        print(root.val)
        self.InOrder(root.right)

    def InOrderIntensive(self, root: TreeNode):
        q = collections.deque()
        q.append(root)
        while len(q) > 0:
            curr = q.pop()
            print(curr.val)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)


if __name__ == "__main__":
    tree = TreeNode('F', TreeNode('B', TreeNode('A'), TreeNode('D', TreeNode('C'), TreeNode('E'))),
                    TreeNode('G', None, TreeNode('I', TreeNode('H'))))
    test = TreeTraversal()
    print("\nInOrder Recursive: ")
    test.InOrder(tree)
    print("\nInOrder Intensive: " )
    test.InOrderIntensive(tree)
