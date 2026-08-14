class Queue:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Queue size must be greater than zero.")

        self.front = -1
        self.rear = -1
        self.data = [None] * size
        self.MaxSize = size

    def is_Empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.MaxSize - 1

    def reset(self):
        self.front = -1
        self.rear = -1
        self.data = [None] * self.MaxSize

    def Enequeue(self, item):
        if self.is_full():
            print("The queue is full.")
            return False

        self.rear += 1
        self.data[self.rear] = item

        return True

    def enqueue(self, item):
        return self.Enequeue(item)

    def dequeue(self):
        if self.is_Empty():
            print("The queue is empty.")
            return None

        self.front += 1
        result = self.data[self.front]
        self.data[self.front] = None

        if self.front == self.rear:
            self.reset()

        return result

    def get_fron(self):
        if self.is_Empty():
            print("The queue is empty.")
            return None

        return self.data[self.front + 1]

    def get_front(self):
        return self.get_fron()

    def get_rear(self):
        if self.is_Empty():
            print("The queue is empty.")
            return None

        return self.data[self.rear]

    def deletitem(self, item):
        if self.is_Empty():
            print("The queue is empty.")
            return False

        start = self.front + 1

        while start <= self.rear:
            if self.data[start] == item:
                index = start

                while index < self.rear:
                    self.data[index] = self.data[index + 1]
                    index += 1

                self.data[self.rear] = None
                self.rear -= 1

                if self.rear == self.front:
                    self.reset()

                return True

            start += 1

        print(f"Item {item} was not found.")
        return False

    def deleteitem(self, item):
        return self.deletitem(item)

    def display(self):
        if self.is_Empty():
            print("The queue is empty.")
            return

        print("Queue elements:")

        index = self.front + 1

        while index <= self.rear:
            print(self.data[index])
            index += 1

    def get_size(self):
        if self.is_Empty():
            return 0

        return self.rear - self.front

    def is_empty(self):
        return self.is_Empty()

    def __len__(self):
        return self.get_size()
