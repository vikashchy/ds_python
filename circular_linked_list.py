class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CrcularLinkedList:  # todo implementation pending
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

    def delete(self, value):
        if self.start.value == value:
            self.start = self.start.next
            return
        current = self.start
        last_node = None
        while current:
            if current.value == value:
                last_node.next = current.next
                return
            else:
                last_node = current
                current = current.next


linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)
linked_list.print()
linked_list.delete(20)
linked_list.print()
