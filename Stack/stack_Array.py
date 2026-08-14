class Stack:
    def __init__(self, maxSize):
        if maxSize <= 0:
            raise ValueError("Stack size must be greater than zero.")

        self.Top = -1
        self.data = [None] * maxSize
        self.MaxSize = maxSize

    def isEmpty(self):
        return self.Top == -1

    def isfull(self):
        return self.Top == self.MaxSize - 1

    def is_empty(self):
        return self.isEmpty()

    def is_full(self):
        return self.isfull()

    def push(self, item):
        if self.isfull():
            print("Stack overflow.")
            return False

        self.Top += 1
        self.data[self.Top] = item
        return True

    def pop(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None

        value = self.data[self.Top]
        self.data[self.Top] = None
        self.Top -= 1

        return value

    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None

        return self.data[self.Top]

    def display(self):
        if self.isEmpty():
            print("Stack is empty.")
            return

        print("Stack elements:")

        for i in range(self.Top, -1, -1):
            print(self.data[i])

    def TransStack(self):
        if self.isEmpty():
            print("Stack is empty.")
            return Stack(1)

        original_size = self.Top + 1
        result = Stack(original_size)

        temp = []

        while not self.isEmpty():
            temp.append(self.pop())

        for value in temp:
            self.push(value)

        for value in reversed(temp):
            result.push(value)

        return result

    def deleteElement(self, val):
        if self.isEmpty():
            print("Stack is empty.")
            return False

        if val not in self.data[:self.Top + 1]:
            print(f"Value {val} was not found.")
            return False

        temp = []

        while not self.isEmpty():
            value = self.pop()

            if value == val:
                break

            temp.append(value)

        while temp:
            self.push(temp.pop())

        return True

    def search(self, val):
        if self.isEmpty():
            return -1

        for i in range(self.Top, -1, -1):
            if self.data[i] == val:
                return i

        return -1

    def get_size(self):
        return self.Top + 1

    def clear(self):
        self.Top = -1
        self.data = [None] * self.MaxSize

    def __len__(self):
        return self.get_size()

    def __str__(self):
        return str(self.data[:self.Top + 1])
