class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def swapPair(node: Node):
    dummy = Node(0)
    dummy.next = node
    current = dummy

    while current.next and current.next.next:
        first_node = current.next
        second_node = current.next.next

        first_node.next = second_node.next
        current.next = second_node
        current.next.next = first_node
        current = current.next.next

    return current.next


if __name__ == "__main__":
    node = Node(1, Node(2, Node(3, Node(4))))

    l2 = swapPair(node)
    list_item = ""
    while l2:
        list_item += str(l2.val) + "-->"
        l2 = l2.next

    print(list_item)
