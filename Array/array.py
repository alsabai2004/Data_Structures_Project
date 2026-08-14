class Arrays:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Array size cannot be negative.")

        self.data = []
        self.size = size

    def insert(self):
        print("Enter array elements:")

        self.data.clear()

        for i in range(self.size):
            while True:
                try:
                    value = int(input(f"Enter value {i + 1}: "))
                    self.data.append(value)
                    break
                except ValueError:
                    print("Please enter a valid integer.")

    def display(self):
        if not self.data:
            print("Array is empty.")
            return

        print("Array elements:")

        for value in self.data:
            print(value)

    def deleteitem(self, item):
        if item not in self.data:
            print(f"Value {item} was not found.")
            return False

        self.data.remove(item)
        self.size = len(self.data)

        print(f"Value {item} deleted successfully.")
        return True

    def deleteALLItem(self, item):
        if item not in self.data:
            print(f"Value {item} was not found.")
            return False

        count = self.data.count(item)

        self.data = [value for value in self.data if value != item]
        self.size = len(self.data)

        print(f"Deleted {count} occurrence(s) of {item}.")
        return True

    def notfirst(self, item):
        if item not in self.data:
            print(f"Value {item} was not found.")
            return False

        first_index = self.data.index(item)

        new_data = []

        for index, value in enumerate(self.data):
            if value != item or index == first_index:
                new_data.append(value)

        removed_count = len(self.data) - len(new_data)

        self.data = new_data
        self.size = len(self.data)

        print(
            f"Deleted {removed_count} occurrence(s) of {item}, "
            "keeping the first occurrence."
        )

        return True

    def search(self, item):
        return item in self.data

    def get_length(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def clear(self):
        self.data.clear()
        self.size = 0

    def get(self, index):
        if index < 0 or index >= len(self.data):
            print("Index out of range.")
            return None

        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)
