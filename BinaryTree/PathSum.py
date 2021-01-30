class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def pathsum(root: TreeNode, value):
    h = []
    sum1 = 0

    def postorder(root: TreeNode, sum1):
        if root is None:
            return
        sum1 += root.val
        h.append(sum1)
        postorder(root.left, sum1)
        postorder(root.right, sum1)


    postorder(root, sum1)
    # if value in h:
    #     return True
    # else:
    #     return False

    return max(h)

def pathsum1(root: TreeNode, sum):
    if not root:
        return False
    elif not root.left and not root.right:
        if root.val == sum:
            return True
        else:
            return False
    return pathsum1(root.left, sum - root.val) or pathsum1(root.right, sum - root.val)




if __name__ == "__main__":
    tree = TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(5)), TreeNode(5, None, TreeNode(5)))
    tree2 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    tree3 = TreeNode(1)

    print(pathsum1(tree2, 22))
    print(pathsum(tree2, 22))


