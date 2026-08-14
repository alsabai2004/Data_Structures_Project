class PriorityQueue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, item, priority):
        self.data.append((priority, item))
        self.data.sort(key=lambda x: x[0])

    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.pop(0)[1]

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0][1]

    def size(self):
        return len(self.data)

    def clear(self):
        self.data.clear()

    def to_list(self):
        return [item for priority, item in self.data]
