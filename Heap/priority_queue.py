class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def enqueue(self, value, priority):
        item = (priority, value)
        self.heap.append(item)
        i = len(self.heap) - 1

        while i > 0:
            parent = self._parent(i)
            if self.heap[parent][0] <= self.heap[i][0]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def dequeue(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()[1]

        item = self.heap[0]
        self.heap[0] = self.heap.pop()

        i = 0

        while True:
            left = self._left(i)
            right = self._right(i)
            smallest = i

            if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

        return item[1]

    def peek(self):
        return self.heap[0][1] if self.heap else None

    def is_empty(self):
        return not self.heap

    def size(self):
        return len(self.heap)

    def display(self):
        print(self.heap)

    def clear(self):
        self.heap.clear()
