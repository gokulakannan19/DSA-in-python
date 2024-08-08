class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        current_node = self.head
        if current_node == self.tail:
            self.head = self.tail = None
            return current_node
        while current_node != None and current_node.next.next != None:
            current_node = current_node.next
        element = current_node.next
        current_node.next = None
        self.tail = current_node
        return element

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.tail

    def isEmpty(self):
        return bool(self.head == None)

    def minValue(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        current_node = minimum = self.head
        while current_node.next != None:
            current_node = current_node.next
            print(minimum.data, current_node.data)
            if minimum.data > current_node.data:
                minimum = current_node
            # print("entered")
            # print(min.data, current_node.next.data)
            # if min.data < current_node.next.data:
            # current_node = current_node.next
        print(minimum.data)
        return minimum

    def printStack(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data, end="->")
            current_node = current_node.next
        print()


llstack = Stack()
llstack.push(30)
llstack.push(20)
llstack.push(10)
llstack.pop()
# llstack.minValue()
llstack.pop()
# llstack.minValue()
# llstack.pop()
# llstack.minValue()
# llstack.printStack()
# print(llstack.head.data)
# print(llstack.tail.data)


llstack2 = Stack()
llstack2.push(50)
llstack2.push(40)
# llstack2.printStack()
# llstack2.minValue()
llstack2.push(30)
llstack2.push(20)
llstack2.push(10)
llstack2.printStack()
# llstack2.minValue()
llstack2.pop()
llstack2.printStack()
# llstack2.minValue()
llstack2.pop
# llstack.minValue()
llstack2.pop()
llstack2.pop()
# llstack2.minValue()
llstack2.pop()

llstack2.printStack()
llstack2.minValue()
