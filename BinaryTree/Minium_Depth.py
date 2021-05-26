class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def minimumDepth(root):
    # Null node has 0 depth.
    if root == None:
        return 0

    # Initialize a list to be used a queue with the root.
    q = []
    q.append({'node': root, 'depth': 1})

    # Level order traversal algorithm:
    while (len(q)):
        # Get the node at the front of the queue.
        queueItem = q.pop(0)

        # Retreive the data that the node had
        node = queueItem['node']
        depth = queueItem['depth']

        # If this is the first leaf node encountered,
        # return its depth and terminate the algorithm.
        if node.left == None and node.right == None:
            return depth

            # If left subtree exists, add it to queue
        if not node.left == None:
            q.append({'node': node.left, 'depth': depth + 1})

            # if right subtree exists, add it to queue
        if not node.right == None:
            q.append({'node': node.right, 'depth': depth + 1})

        # Driver code


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.right.left.right = Node(7)
print("The min depth is:", minimumDepth(root))