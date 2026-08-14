from models.node import Node


class QueueLinked:
    def __init__(self):
        self.Front = None
        self.Rear = None

    def is_empty(self):
        return self.Front is None

    def Enequeue(self, item):
        new_node = Node(item)

        if self.Front is None:
            self.Front = new_node
            self.Rear = new_node
            return True

        self.Rear.Next = new_node
        self.Rear = new_node

        return True

    def Dequeue(self):
        if self.Front is None:
            print("The queue is empty.")
            return None

        temp = self.Front
        self.Front = self.Front.Next
        temp.Next = None

        if self.Front is None:
            self.Rear = None

        return temp.data

    def get_size(self):
        counter = 0
        temp = self.Front

        while temp is not None:
            counter += 1
            temp = temp.Next

        return counter

    def get_length(self, mnode=None):
        if mnode is None:
            return 0

        return 1 + self.get_length(mnode.Next)

    def getFront(self):
        if self.Front is None:
            return None

        return self.Front.data

    def getRear(self):
        if self.Rear is None:
            return None

        return self.Rear.data

    def display(self):
        if self.Front is None:
            print("The queue is empty.")
            return

        temp = self.Front

        while temp is not None:
            print(temp.data)
            temp = temp.Next

    def clear(self):
        self.Front = None
        self.Rear = None

    def __len__(self):
        return self.get_size()
