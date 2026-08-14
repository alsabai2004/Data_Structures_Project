class MinHeap:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _up(self, i):
        while i > 0:
            p = self._parent(i)
            if self.data[p] <= self.data[i]:
                break
            self.data[p], self.data[i] = self.data[i], self.data[p]
            i = p

    def _down(self, i):
        while True:
            left = self._left(i)
            right = self._right(i)
            smallest = i

            if left < len(self.data) and self.data[left] < self.data[smallest]:
                smallest = left

            if right < len(self.data) and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == i:
                break

            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest

    def insert(self, value):
        self.data.append(value)
        self._up(len(self.data) - 1)

    def peek(self):
        return None if self.is_empty() else self.data[0]

    def extract_min(self):
        if self.is_empty():
            return None

        if len(self.data) == 1:
            return self.data.pop()

        result = self.data[0]
        self.data[0] = self.data.pop()
        self._down(0)
        return result

    def clear(self):
        self.data.clear()

    def to_list(self):
        return self.data.copy()
