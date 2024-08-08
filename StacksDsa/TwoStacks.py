class TwoStacks:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top1 = -1
        self.top2 = self.capacity

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.items[self.top1] = data
        else:
            print("Stack overflow")
            exit(1)

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.items[self.top2] = data
        else:
            print("Stack overflow")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.items[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack underflow")
            exit(1)

    def pop2(self):
        if self.top2 < self.capacity:
            x = self.items[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow")
            exit(1)


ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))
