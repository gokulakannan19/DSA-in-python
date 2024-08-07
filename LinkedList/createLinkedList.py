class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFirst(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def addLast(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def insertAt(self, index, data):
        if index == 0:
            self.addFirst(data)
            return
        current_node = self.head
        position = 0
        while current_node != None and position+1 != index:
            current_node = current_node.next
            position += 1
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
            if current_node == self.tail:
                self.tail = new_node
        else:
            print("No index found")
            return

    def updateNode(self, index, value):
        if index == 0:
            self.head.data = value
            return
        current_node = self.head
        position = 0
        while current_node != None and position != index:
            current_node = current_node.next
            position += 1
        if current_node is not None:
            current_node.data = value

    def deleteFirst(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteLast(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node != None and current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node

    def deleteAt(self, index):
        if self.head is None:
            return
        if index > self.sizeOf()-1:
            print("Index out of bounds")
            return
        if index == 0:
            self.deleteFirst()
            return
        current_node = self.head
        position = 0
        while current_node != None and position+1 != index:
            current_node = current_node.next
            position += 1
        if current_node != None:
            if current_node.next == self.tail:
                self.tail = current_node
            current_node.next = current_node.next.next
        else:
            print("No index found")

    def contains(self, data):
        return True if self.indexOf(data) != -1 else False

    def indexOf(self, data):
        if self.head is None:
            return
        counter = 0
        current_node = self.head
        while current_node != None and current_node.data != data:
            current_node = current_node.next
            counter += 1
        return counter if current_node is not None else -1

    def sizeOf(self):
        if self.head is None:
            return
        counter = 0
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            counter += 1
        return counter

    def convertToList(self):
        if self.head is None:
            return []
        new_list = []
        current_node = self.head
        while current_node != None:
            new_list.append(current_node.data)
            current_node = current_node.next
        return new_list

    def reverse(self):
        if self.head is None:
            return

        previous_node = self.head
        current_node = self.head.next
        # 10 -> 20 -> 30
        # P = 10 , C = 20, N = 30
        while current_node != None:
            next_node = current_node.next  # next = 30
            current_node.next = previous_node  # current.next = 10
            previous_node = current_node  # previous node = 20, none
            current_node = next_node

        self.tail = self.head
        self.tail.next = None
        self.head = previous_node

    def getKthFromTheEnd(self, k):
        if self.head is None:
            return

        current_node = self.head
        first = second = current_node

        for i in range(0, k-1):
            second = second.next
            if second == None:
                print("Exception occur. Node becomes none. No value")
                return

        while second != self.tail:
            print(first.data, second.data)
            first = first.next
            second = second.next

        print(first.data)
        return first.data

    def printMiddle(self):
        if self.head is None:
            return

        first_node = second_node = self.head

        while second_node != self.tail and second_node.next != self.tail:
            second_node = second_node.next.next
            first_node = first_node.next

        if second_node == self.tail:
            print(first_node.data)
        else:
            print(f"{first_node.data}, {first_node.next.data}")

    def hasLoop(self):
        if self.head is None:
            return

        # creating a loop for this example
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = self.head

        fast_pointer = slow_pointer = self.head
        while fast_pointer != None and slow_pointer != None and fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

    def printLL(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data, end="->")
            current_node = current_node.next
        print()


llist = LinkedList()
llist.addFirst(10)
llist.addFirst(20)
llist.addFirst(30)
llist.printLL()
print("**********************************")
llist.addLast(100)
llist.addLast(200)
llist.printLL()
print("**********************************")
llist.deleteFirst()
llist.deleteLast()
llist.printLL()
print("**********************************")
print(llist.indexOf(10))
print(llist.indexOf(100))
print(llist.contains(10))
print(llist.contains(1000))
print(llist.sizeOf())
print("**********************************")
llist.insertAt(0, 500)
llist.insertAt(4, 500)
llist.printLL()
print("**********************************")
llist.updateNode(4, 600)
llist.printLL()
print("**********************************")
print(llist.sizeOf())
llist.deleteAt(4)
llist.printLL()
print("**********************************")
print(llist.convertToList())
print("**********************************")
# llist.reverse()
# llist.printLL()
llist.getKthFromTheEnd(6)
print("***********************************")
llist.addFirst(50)
llist.addFirst(60)
llist.printLL()
llist.printMiddle()
print("************************************")
llist.deleteFirst()
llist.printLL()
print(llist.hasLoop())
print("HEAD ->", llist.head.data)
print("TAIL ->", llist.tail.data)


print("*****************************************************************************")
llist2 = LinkedList()
llist2.addFirst(10)
llist2.addLast(20)
llist2.addLast(30)
llist2.addLast(40)
llist2.addLast(50)
llist2.addLast(60)
llist2.printLL()
print(llist2.hasLoop())
