class Queue:
    def __init__(self):
        self.elements = list()
        self.start = -1
        self.end = -1

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        if self.elements:
            self.elements.pop(0)
        else:
            print("Nothing to pop")


que = Queue()
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
