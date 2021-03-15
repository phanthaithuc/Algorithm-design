from Linkedlist import MyLinkedList
from Linkedlist import Node


def deep_copy(head: Node) -> None:
    source = {None: None}
    curr = head
    while curr:
        copy = curr.val
        source[curr] = copy
        curr = curr.next

    current = head
    while current:
        copy = source[current]
        copy.next = source[current.next]
        copy.random = source[current.random]
        current = current.next

    return source[head]


if __name__ == '__main__':
    test = Node(1, Node(2, Node(4), Node(5)), Node(3))
    MyLinkedList().print(test)
