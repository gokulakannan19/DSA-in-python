class stackQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Stack is empty")
            exit(1)

        self.moveStack1ToStack2()

        return self.stack2.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            exit(1)

        self.moveStack1ToStack2()

        return self.stack2[-1]

    def isEmpty(self):
        return True if not self.stack1 and not self.stack2 else False

    def moveStack1ToStack2(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


sq = stackQueue()
sq.enqueue(10)
sq.enqueue(20)
sq.enqueue(30)

print(sq.stack1 + sq.stack2)
# print(sq.stack1)
# print(sq.stack2)
print(sq.peek())
# print(sq.dequeue())
# print(sq.dequeue())
# print(sq.dequeue())
# print(sq.dequeue())
