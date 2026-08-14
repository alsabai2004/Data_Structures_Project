class CircularQueue:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Queue size must be positive.")
        self.data = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0
        self.max_size = size

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.data[self.rear] = item
        self.count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.data[self.front]

    def size(self):
        return self.count

    def clear(self):
        self.data = [None] * self.max_size
        self.front = 0
        self.rear = -1
        self.count = 0

    def to_list(self):
        return [
            self.data[(self.front + i) % self.max_size]
            for i in range(self.count)
        ]
