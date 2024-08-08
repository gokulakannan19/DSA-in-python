class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.counter = 0

    def push(self, data):
        if self.counter == self.capacity:
            print("Stack is full")
            return -1
        self.items[self.counter] = data
        self.counter += 1
        print(self.items)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        element = self.items[self.counter-1]
        self.counter -= 1
        return element

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
            return
        element = self.items[self.counter-1]
        # print(element)
        return element

    def isEmpty(self):
        return bool(self.counter == 0)

    def minValue(self):
        if self.isEmpty():
            print("Array is empty")
            return
        minimum = self.items[0]
        for i in range(self.counter):
            if minimum > self.items[i]:
                minimum = self.items[i]
        print(minimum)

    def printStack(self):
        for i in range(self.counter):
            print(self.items[i], end="->")
        print()


array_stack = Stack(5)
print(array_stack.isEmpty())
array_stack.push(10)
array_stack.push(20)
array_stack.push(30)
array_stack.push(40)
array_stack.minValue()
array_stack.push(50)
array_stack.push(60)
print(array_stack.peek())
array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()
print(array_stack.peek())
print("**************************")
array_stack.printStack()
array_stack.minValue()
# array_stack.push(10)
array_stack.printStack()
