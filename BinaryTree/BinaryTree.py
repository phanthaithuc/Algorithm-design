class TreeNode:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right


# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

def BSTSortedOrder(nums: []):
    if not nums:
        return
    n = len(nums)
    if n == 1:
        root = TreeNode(nums[0])
        return root
    if n == 2:
        root = TreeNode(nums[0])
        root.right = TreeNode(nums[1])
        return root

    mid = n // 2
    root = TreeNode(nums[mid])
    left = BSTSortedOrder(nums[:mid])
    right = BSTSortedOrder(nums[mid + 1:])
    root.left = left
    root.right = right

    return root


def printnode(root: TreeNode, level=0):
    if not root:
        return
    printnode(root.right, level + 1)
    print("  " * 4 * level + ' |-->', root.val)
    printnode(root.left, level + 1)


def treelevel(root: TreeNode, level=0):
    if not root:
        return
    treelevel(root.right, level + 1)
    print("right level = ", level)
    treelevel(root.left, level + 1)
    print("left level = ", level)


if __name__ == "__main__":
    nums = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    tree = BSTSortedOrder(nums)
    printnode(tree)
    treelevel(tree)
