class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insert(self, value):
        if self.start is None:
            self.start = Node(value)
            return
        current = self.start
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def print(self):
        current = self.start
        while current:
            print(current.value)
            print(current.next)
            current = current.next


linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)
linked_list.print()
