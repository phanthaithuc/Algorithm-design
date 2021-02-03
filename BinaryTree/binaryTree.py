import collections
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


#          a
#       /    \
#     b        c
#   /   \       \
# d      e        f

def bfs(root: Node):
    if root is None:
        return None
    q = collections.deque()
    q.append(root)
    res = []
    while len(q) > 0:
        curr = q.popleft()
        res.append(curr.value)
        if curr.left is not None:
            # print("/n", curr.left.value)
            q.append(curr.left)
        if curr.right is not None:
            # print("/n", curr.right.value)
            q.append(curr.right)

    return res


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    t = Node(3, Node(1), Node(2))

    print(bfs(a))
