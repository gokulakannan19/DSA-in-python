class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.count = 0

    # Method to insert
    def insert(self, data):
        if self.isFull():
            new_capacity = self.count * 2
            new_array = Array(new_capacity)
            for index in range(self.count):
                new_array.items[index] = self.items[index]
            self.items = new_array.items

        self.items[self.count] = data
        self.count += 1

    # Method to remove at specific index
    def removeAt(self, index):
        if index < 0 or index >= self.count:
            print("Invalid index position")
            return
        for i in range(index, self.count):
            self.items[i] = self.items[i+1]
        self.count -= 1

    # Method to find index of data
    def indexOf(self, data):
        if self.isEmpty():
            print("Array is empty")
            return
        for index in range(self.count):
            # print(self.items[index])
            if data == self.items[index]:
                print(index)
                return
        print("No data found")
        return

    # Method to find the largest nuber of the array
    def max(self):
        if not self.isEmpty():
            big = self.items[0]
            for index in range(1, self.count):
                if self.items[index] > big:
                    big = self.items[index]
            print(big)
            return big
        print("Array is empty")

    # Method to find the common elements in both array
    def intersect(self, second_array):
        for i in self.items:
            for j in second_array:
                if i == j:
                    print(i, end=" ")
        print()

    # Method to reverse an array
    def reverse(self):
        for index in range(self.count-1, -1, -1):
            print(self.items[index], end=" ")
        print()

    # Method to insert at specific index
    def insertAt(self, index, data):
        if index < 0 or index > self.count:
            raise IndexError("Index out of bounds")

        if self.isFull():
            self.resize()

        for i in range(self.count, index, -1):
            self.items[i] = self.items[i - 1]
        self.items[index] = data
        self.count += 1

    # Method to resize the array
    def resize(self):
        """Resizes the array by doubling its capacity."""
        new_capacity = self.count * 2
        new_array = Array(new_capacity)
        for i in range(self.count):
            new_array.items[i] = self.items[i]
        self.items = new_array.items

    def printArray(self):
        for index in range(self.count):
            print(self.items[index], end=" ")
        print()

    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    def isFull(self):
        if self.count == self.capacity:
            return True
        return False


array = Array(5)
array.max()
# array.insert(10)
array.insert(-10)
array.insert(-20)
array.insert(-30)
array.insert(-40)
array.insert(-50)
array.insert(-60)
array.insert(0)
array.removeAt(5)
# array.insert(70)
array.removeAt(0)
array.removeAt(2)
array.printArray()
array.indexOf(3000)
array.indexOf(30)
array.max()
array.printArray()
# array.intersect([0, -20, 50, 70, 90])
array.reverse()

print("**************************")

array2 = Array(5)
array2.insert(5)
array2.insert(10)
# array2.printArray()
# array2.insertAt(2, 100)
array2.insert(20)
array2.insert(30)
array2.insert(40)
array2.insertAt(6, 60)
# array2.insertAt(6, 60)
# array2.insertAt(6, 6000)
# array2.insertAt(0, 1000)
array2.printArray()
