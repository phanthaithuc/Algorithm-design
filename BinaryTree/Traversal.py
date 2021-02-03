import collections


# Preorder:
# <root> <left> <right>
#
# Inorder:
# <left> <root> <right>
#
# Postorder:
# <left> <right> <root>


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeTraversal:
    # Inorder:
    # <left> <root> <right>
    def InOrder(self, root: TreeNode):
        if root is None:
            return
        self.InOrder(root.left)
        print(root.val)
        self.InOrder(root.right)

    # Inorder:
    # <left> <root> <right>
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

    # Postorder:
    # <left> <right> <root>

    def PostOrder(self, root: TreeNode):
        if root is None:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.val)

    # Preorder:
    # <root> <left> <right>

    def PreOrder(self, root: TreeNode):
        if root is None:
            return

        print(root.val)
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def findHeight(self, root: TreeNode):
        if root is None:
            return -1
        leftHeight = self.findHeight(root.left) + 1
        rightHeight = self.findHeight(root.right) + 1
        return max(leftHeight, rightHeight)
        # return max(self.findHeight(root.left), self.findHeight(root.right)) + 1

    # def levelOrder(self, root: TreeNode):
    #
    #     res = []
    #     q = collections.deque()
    #     q.append(root)
    #     while q:
    #         current_node = q[0]
    #         if current_node.left is not None:
    #             q.append(current_node.left)
    #         if current_node.right is not None:
    #             q.append(current_node.right)
    #         res.append(current_node.val)
    #         q.popleft()
    #
    #     return res

    def levelValue(self, root: TreeNode):
        if root is None:
            return

        q = collections.deque()
        q.append(root)
        res = []
        height = 0
        while q:
            row = []
            rowSize = len(q)
            while rowSize > 0:
                curr = q.popleft()
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
                row.append(curr.val)
                rowSize -= 1
            res.append(row)
        return res, height

    def levelOrder(self, root: TreeNode):
        if root is None:
            return
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            curr = q[0]
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
            temp = q.popleft()
            res.append(temp.val)

        return res

    # Preorder <root> <left> <right>
    # Preorder is Depth First Search
    def PreOrderIterative(self, root: TreeNode):
        stack = collections.deque()
        stack.append(root)
        res = []
        while stack:
            curr = stack.pop()
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
            res.append(curr.val)
        return res

    def print_tree(self, root: TreeNode, level=0):
        if not root:
            return
        self.print_tree(root.right, level + 1)
        print('  ' * 4 * level + '     --> ', root.val)
        self.print_tree(root.left, level + 1)


if __name__ == "__main__":
    tree = TreeNode('F', TreeNode('B', TreeNode('A'), TreeNode('D', TreeNode('C'), TreeNode('E'))),
                    TreeNode('G', None, TreeNode('I', TreeNode('H'))))

    tree_2 = TreeNode("F", TreeNode("B", TreeNode("A"), TreeNode("D", TreeNode("C"), TreeNode("E"))),
                      TreeNode("G", TreeNode("T"), TreeNode("I", TreeNode("H"))))
    travel = TreeTraversal()
    print("InOrder Recursive: ")
    travel.InOrder(tree_2)
    print("InOrder Intensive: ")
    travel.InOrderIntensive(tree_2)

    print("PostOrder Recursive: ")
    travel.PostOrder(tree_2)

    print("PreOrder Recursive: ")
    travel.PreOrder(tree_2)
    res = travel.PreOrderIterative(tree_2)
    print("Preorder Intensive:", res)

    print("Height of the tree: ", travel.findHeight(tree_2))
    print("Level Order tree: ")
    print(travel.levelOrder(tree_2))
    print('\n Row level of value: ')
    value, height = travel.levelValue(tree)
    print("\n Value of each level tree:", value)
    print('\n Height of the tree: ', len(value))
    travel.print_tree(tree)


