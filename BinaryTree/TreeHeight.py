from Traversal import TreeNode

def tree_height(root: TreeNode):
    if not root:
        return -1
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)

def depth(root: TreeNode) -> int:
    if not root:
        return 0
    hl = depth(root.left) + 1
    hr = depth(root.right) + 1
    if abs(hl - hr) > 1:
        raise Exception("Sorry, the tree is unbalanced")
    else:
        return max(hl, hr)


def isBalanced(root: TreeNode) -> bool:
    try:
        depth(root)
    except:
        return False
    return True


if __name__ == "__main__":
    tree = TreeNode(1)
    tree2 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                     TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    print(tree_height(tree2))
    print(depth(tree2))
