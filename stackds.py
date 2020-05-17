class Stack:
    def __init__(self):
        self.elements = list()

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        if len(self.elements) < 1:
            print('Stack empty')
        else:
            self.elements.pop()

    def print(self):
        return [elem for elem in self.elements]


stck = Stack()
stck.push(10)
stck.push(20)
stck.push(30)
stck.push(40)
stck.pop()
print(stck.print())
