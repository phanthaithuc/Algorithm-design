class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1009  # use prime number
        self.set = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        bucket = self._hash(key)
        new = LinkNode(key)
        if self.set[bucket]:
            new.next = self.set[bucket]
        self.set[bucket] = new

    def remove(self, key: int) -> None:
        # remove is to search value in a linkedlist
        bucket = self._hash(key)
        if not self.set[bucket]:
            return
        head = self.set[bucket]
        if head.val == key:
            self.set[bucket] = head.next
        else:
            while head:
                if head.val == key:
                    prev.next = head.next
                prev = head
                head = head.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = self._hash(key)
        if not self.set[bucket]:
            return False
        node = self.set[bucket]
        while node:
            if node.val == key:
                return True
            node = node.next
        else:
            return False