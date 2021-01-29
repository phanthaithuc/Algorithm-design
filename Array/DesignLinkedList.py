class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size+=1

    def print(self):
        if self.head is None:
            print("Empty Linked list")
        list_item = ""
        itr = self.head
        while itr:
            list_item += str(itr.data) + "-->"
            itr = itr.next
        print(list_item)

    def get_length(self):
        if self.head is None:
            raise Exception("Empty Linked list")
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def get(self, index: int) -> int:
        if self.head is None:
            print("Empty Linked list")
            return -1
        if index > self.get_length() - 1 or index < 0:
            print("index out of range")
            return -1
        count = 0
        itr = self.head
        value = 0

        while itr:
            if count == index:
                value = itr.data
            itr = itr.next
            count += 1
        return value

    def addAtIndex(self, index: int, val: int) -> None:

        if self.head is None:
            self.addAtHead(val)
            return

        if index > self.get_length() or index < 0:
            return

        itr = self.head
        count = 0
        while itr:
            if index == 0:
                self.addAtHead(val)
            elif count == index - 1:
                node = Node(val, itr.next)
                itr.next = node
                self.size += 1
            count += 1
            itr = itr.next

    def deleteAtindex(self, index: int) -> None:
        if index > self.get_length() - 1 or index < 0:
            return
        itr = self.head
        count = 0
        while itr:
            if index == 0:
                self.head = self.head.next
                self.size -= 1
                break
            elif count == index - 1:
                itr.next = itr.next.next
                self.size -= 1
            count += 1
            itr = itr.next

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.addAtHead(val)
            return
        else:
            itr = self.head
            count = 0
            length = self.get_length()
            while itr:
                if count == length - 1:
                    node = Node(val, None)
                    itr.next = node
                    self.size += 1

                count += 1
                itr = itr.next

    def get_length_self(self):
        return self.size

    def is_cycle(self):
        itr = self.head
        dictionary = {}
        pos = 0
        while itr:
            if itr in dictionary:
                return True
            else:
                dictionary[itr] = pos
                pos += 1
            itr = itr.next

        print(dictionary)
        return False

    def is_cycle_2(self):
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def is_cycle_3(self):
        seen = {}
        itr = self.head
        while itr:
            if itr in seen:
                return itr
            else:
                seen[itr] = True
            itr = itr.next
        return False

    def remove_from_end(self, index:int) -> None:
        if index < 0 or index > self.size:
            return
        count = 0
        itr = self.head
        while itr:
            if count == self.size - index - 1:
                self.deleteAtindex(count)
            count+=1
            itr = itr.next


if __name__ == "__main__":
    index = 2
    ll = LinkedList()
    ll.addAtHead(7)
    ll.addAtHead(2)
    ll.addAtHead(1)
    ll.addAtIndex(3, 0)
    ll.deleteAtindex(2)
    ll.addAtHead(6)
    ll.addAtTail(4)
    print(ll.get(4))
    ll.addAtHead(4)
    ll.addAtIndex(5, 0)
    ll.addAtHead(6)
    ll.print()

    ll.remove_from_end(-1)
    ll.print()




