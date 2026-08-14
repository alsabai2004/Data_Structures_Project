class HashTable:
    def __init__(self, capacity=10):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity = capacity
        self.data = [[] for _ in range(capacity)]
        self.count = 0

    def _index(self, key):
        return hash(key) % self.capacity

    def set(self, key, value):
        bucket = self.data[self._index(key)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return False

        bucket.append((key, value))
        self.count += 1
        return True

    def get(self, key, default=None):
        for k, v in self.data[self._index(key)]:
            if k == key:
                return v
        return default

    def remove(self, key):
        bucket = self.data[self._index(key)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return v

        return None

    def contains(self, key):
        return self.get(key, object()) is not None

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def clear(self):
        self.data = [[] for _ in range(self.capacity)]
        self.count = 0

    def keys(self):
        return [k for bucket in self.data for k, v in bucket]

    def values(self):
        return [v for bucket in self.data for k, v in bucket]
