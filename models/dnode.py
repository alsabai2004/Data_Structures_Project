class DNode:
    def __init__(self, data):
        self.data = data
        self.Next = None
        self.prav = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"DNode({self.data!r})"
