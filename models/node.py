class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Node({self.data!r})"
