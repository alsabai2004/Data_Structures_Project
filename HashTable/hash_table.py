class HashTable:
    def __init__(self, size=10):
        if size <= 0:
            raise ValueError("Hash table size must be positive.")
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return False

        self.table[index].append([key, value])
        return True

    def search(self, key):
        index = self._hash(key)

        for stored_key, value in self.table[index]:
            if stored_key == key:
                return value

        return None

    def delete(self, key):
        index = self._hash(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True

        return False

    def contains(self, key):
        return self.search(key) is not None

    def keys(self):
        return [pair[0] for bucket in self.table for pair in bucket]

    def values(self):
        return [pair[1] for bucket in self.table for pair in bucket]

    def items(self):
        return [(pair[0], pair[1]) for bucket in self.table for pair in bucket]

    def is_empty(self):
        return all(not bucket for bucket in self.table)

    def clear(self):
        self.table = [[] for _ in range(self.size)]

    def get_size(self):
        return sum(len(bucket) for bucket in self.table)

    def display(self):
        if self.is_empty():
            print("Hash table is empty.")
            return

        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")

    def __len__(self):
        return self.get_size()

    def __str__(self):
        return str(self.items())
