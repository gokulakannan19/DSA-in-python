class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.items = [0] * capacity
        self.items = []
        self.counter = 0

    def add(self, data):

        # Shifting items
        i = 0
        for i in range(self.counter-1, -1, -1):
            if self.items[i] > data:
                self.items[i+1] = self.items[i]
            else:
                break
        self.items[i+1] = data
        self.counter += 1

    def isEmpty(self):
        return True if self.counter == 0 else False

    def printQueue(self):
        for i in range(self.capacity):
            print(self.items[i], end="->")
        print()


pq = PriorityQueue(5)
pq.add(5)
pq.add(3)
pq.printQueue()
