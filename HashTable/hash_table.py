class HashTable:
    def __init__(self, capacity=10):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)

        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                self.table[index][i] = (key, value)
                return False

        self.table[index].append((key, value))
        self.count += 1
        return True

    def search(self, key):
        index = self._hash(key)

        for existing_key, value in self.table[index]:
            if existing_key == key:
                return value

        return None

    def contains(self, key):
        index = self._hash(key)
        return any(existing_key == key for existing_key, _ in self.table[index])

    def delete(self, key):
        index = self._hash(key)

        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                self.table[index].pop(i)
                self.count -= 1
                return True

        return False

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def clear(self):
        self.table = [[] for _ in range(self.capacity)]
        self.count = 0

    def display(self):
        if self.is_empty():
            print("Hash Table is empty.")
            return

        for index, bucket in enumerate(self.table):
            print(f"{index}: {bucket}")
