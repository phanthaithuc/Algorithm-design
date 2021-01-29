import collections
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def BFS(tree: TreeNode):
    res = []
    if tree is None:
        return res

    queue = collections.deque()
    queue.append(tree)
    while queue:
        row = []
        rowSize = len(queue)
        while rowSize > 0:
            currentNode = queue.popleft()
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)
            row.append(currentNode.val)
            rowSize -= 1
        res.append(row)
    return res


def maxDept(root: TreeNode, sum = 0):
    if root is None:
        return sum

    return max(maxDept(root.left, sum + 1), maxDept(root.right, sum + 1))


if __name__ == "__main__":
    tree = TreeNode("F", TreeNode("B", TreeNode("A"), TreeNode("D", TreeNode("C"), TreeNode("E"))),
                    TreeNode("G", None, TreeNode("I", TreeNode("H"))))

    print(maxDept(tree))
    print(BFS(tree))