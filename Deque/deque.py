class Deque:
    def __init__(self):
        self.data = []

    def add_front(self, item):
        self.data.insert(0, item)

    def add_rear(self, item):
        self.data.append(item)

    def remove_front(self):
        if self.is_empty():
            return None
        return self.data.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def front(self):
        return self.data[0] if self.data else None

    def rear(self):
        return self.data[-1] if self.data else None

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def clear(self):
        self.data.clear()

    def display(self):
        print(self.data)
