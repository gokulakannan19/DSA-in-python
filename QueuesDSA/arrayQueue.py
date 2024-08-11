class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full")
            exit(1)

        self.items[self.rear] = data
        self.rear = (self.rear + 1) % len(self.items)
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            exit(1)
        self.items[self.front] = 0
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            exit()
        return self.items[self.front]

    def isEmpty(self):
        return bool(self.count == 0)

    def isFull(self):
        return (bool(self.count == self.capacity))

    def printQueue(self):
        if self.isEmpty():
            print("Emepty queue")
            exit()
        for i in range(self.capacity):
            print(self.items[i], end="->")
        print()


arrqueue = ArrayQueue(5)
arrqueue.enqueue(10)
arrqueue.enqueue(20)
arrqueue.enqueue(30)
arrqueue.enqueue(40)
arrqueue.enqueue(50)
arrqueue.dequeue()
arrqueue.dequeue()
print(arrqueue.capacity)
print(arrqueue.count)
arrqueue.enqueue(60)
print(arrqueue.peek())
arrqueue.printQueue()
