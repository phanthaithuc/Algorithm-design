class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val: int) -> None:  # Method
        node = Node(val, self.head)  # node = (new value, previous head as the "next" value)
        self.head = node

    def print(self):  # Method
        # Check if Linked list is empty or not
        if self.head is None:
            print("empty Linked list")

        # create an empty string to print item in Linked List
        list_item = ""
        itr = self.head

        # loop through the Linked list and print out value
        while itr:
            list_item += str(itr.data) + "-->"
            itr = itr.next

        print(list_item)

    def addAtTail(self, val: int):
        if self.head is None:
            print("Empty Linked list")

        itr = self.head

        # Loop to the end of list
        while itr.next:
            itr = itr.next

        itr.next = Node(val, None)

    def getlength(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def addAtIndex(self, index: int, val) -> None:
        if index < 0 or index >= self.getlength():
            raise Exception("Invalid Index")

        if index == 0:
            node = Node(val, self.head)  # Create new node with the given value
            self.head = node  # add new head = new node with given value, the previous head is now node.next

        flag = 0
        itr = self.head
        while itr:
            if flag == index - 1:
                node = Node(val, itr.next)
                itr.next = node
                break

            itr = itr.next
            flag += 1

    def removeAtIndex(self, index: int) -> None:
        if 0 > index >= self.getlength():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next

        itr = self.head
        flag = 0
        while itr:
            if flag == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            flag += 1

    def getValueAtIndex(self, index: int) -> int:
        if 0 > index > self.getlength():
            raise Exception("Invalid index")

        loop = self.head
        flag = 0
        res = 0
        while loop:
            if flag == index - 1:
                res = loop.next.data
            flag += 1
            loop = loop.next
        return res


def reverse_linkedlist(ListNode: MyLinkedList):
    prev = None
    itr = ListNode.head
    while itr is not None:
        temp = itr.next
        itr.next = prev
        prev = itr
        itr = temp

    final = prev
    list_value = ""
    while final:
        list_value += str(final.data) + "-->"
        final = final.next

    print(list_value)


def merge_sorted_linkedlist(ListNode1: Node, ListNode2: Node):
    a = ListNode1
    b = ListNode2

    if a is not None and b is not None:
        if a.data > b.data:
            a, b = b, a
        a.next = merge_sorted_linkedlist(a.next, b)
    return a or b


def merge_sort(ListNode1: MyLinkedList, ListNode2: MyLinkedList):
    dummy = Node()
    tail = dummy
    l1 = ListNode1.head
    l2 = ListNode2.head
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    list_value = ""
    export = dummy.next
    while export:
        list_value += str(export.data) + "-->"
        export = export.next
    print(list_value)


if __name__ == "__main__":
    ll = MyLinkedList()
    ll.addAtHead(2)
    ll.addAtHead(1)
    ll.addAtTail(4)
    ll.addAtIndex(2, 3)
    ll.addAtTail(7)
    ll.print()
    index = 2

    print("Value at " + str(index) + " index is: " + str(ll.getValueAtIndex(index)))
    print("Reverse Linked List: ")
    reverse_linkedlist(ll)

    ll_2 = MyLinkedList()
    ll_2.addAtHead(4)
    ll_2.addAtHead(2)
    ll_2.addAtHead(1)
    print("\nLinkedList 2: ")
    ll_2.print()

    ll_3 = MyLinkedList()
    ll_3.addAtHead(4)
    ll_3.addAtHead(3)
    ll_3.addAtHead(1)

    print("\nLinkedList 3: ")
    ll_3.print()

    print("\nMerge sorted Linked list: ")
    merge_sort(ll_2, ll_3)

    ll1 = Node(1, Node(2, Node(4)))
    ll2 = Node(1, Node(3, Node(4)))

    print("\nMerge sorted Linked list recursion: ")
    final = merge_sorted_linkedlist(ll1, ll2)
    list_item = ""
    while final:
        list_item += str(final.data) + "-->"
        final = final.next

    print(list_item)
