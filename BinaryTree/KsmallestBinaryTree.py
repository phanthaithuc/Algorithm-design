class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

 #
 # def KSmallest(root: TreeNode) -> int:
 #     if not root:
 #         return




def inOrder(root: TreeNode) -> None:
    if not root:
        return

    res = []
    inOrder(root.left)
    print(root.val);l
    res.append(root.val)
    inOrder(root.right)



if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    result = inOrder(tree)
    print(result)

