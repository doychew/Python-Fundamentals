class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        self.data.append(self.data.pop())

    def top(self):
        pass