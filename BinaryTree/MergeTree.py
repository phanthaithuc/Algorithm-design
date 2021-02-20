from Traversal import TreeTraversal
from Traversal import TreeNode


class Solution(TreeTraversal):
    def __init__(self):
        super(Solution, self).__init__()

    def mergeTree(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return

        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0
        root = TreeNode(v1 + v2)
        root.left = self.mergeTree(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTree(t1.right if t1 else None, t2.right if t2 else None)

        return root


import collections

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def levelOrder(root: Node):
    stack = collections.deque()
    stack.append(root)
    while stack:
        rowSize = len(stack)
        row = []
        while rowSize > 0:
            root = stack.popleft()
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
            row.append(root.val)
            rowSize -= 1
        print(row)




tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

levelOrder(tree)


if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    test = Solution()
    result = test.mergeTree(t1, t2)

    print_out = TreeTraversal()
    print_out.print_tree(result)

    test.InOrder(result)
