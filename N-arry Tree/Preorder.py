import collections


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class NarrayTree_Traversal:

    def preorder_recursive(self, root: Node) -> []:
        if not root:
            return []
        res = []
        root
        res.append(root.val)
        if root.children:
            for children in root.children:
                res += self.preorder_recursive(children)
        return res

    def preorder_intensive(self, root: Node) -> []:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.children:
                for children in curr.children[::-1]:
                    stack.append(children)
        return res

    def postorder_recursive(self, root: Node) -> []:
        if not root:
            return
        res = []
        if root.children:
            for child in root.children:
                res += self.postorder_recursive(child)
        res.append(root.val)
        return res

    def postorder_intensinve(self, root: Node) -> []:
        if not root:
            return []

        stack = collections.deque()
        res = collections.deque()
        stack.append(root)
        while stack:
            curr = stack.popleft()
            if curr.children:
                for children in curr.children:
                    stack.appendleft(children)

            res.appendleft(curr.val)
        return res

    def levelOrder(self, root: Node):
        if not root:
            return

        stack = collections.deque([root])
        res = []
        while stack:
            rowSize = len(stack)
            row = []
            while rowSize > 0:
                curr = stack.popleft()
                if curr.children:
                    for children in curr.children:
                        stack.append(children)
                rowSize -= 1
                row.append(curr.val)
            res.append(row)

        return res

    def depth(self, root: Node) -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        else:
            return 1 + max(self.depth(c) for c in root.children)
            # return 1 + max(self.depth(c) for c in root.children)




if __name__ == "__main__":
    tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

    # # child.children = Node(5)
    # # child.children = Node(6)
    # # tree.children = Node(2)
    # # tree.children = Node(4)
    # # tree.children = child
    # tree.children = [Node(3), Node(2), Node(4)]
    solution = NarrayTree_Traversal()
    print(solution.postorder_intensinve(tree))
    print(solution.preorder_recursive(tree))
    print(solution.levelOrder(tree))
    print(solution.postorder_recursive(tree))
    print(solution.depth(tree))