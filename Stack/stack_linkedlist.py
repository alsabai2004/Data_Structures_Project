from models.node import Node


class Stack_linkedlist:
    def __init__(self):
        self.Top = None

    def push(self, item):
        new_node = Node(item)

        if self.Top is None:
            self.Top = new_node
            return True

        new_node.Next = self.Top
        self.Top = new_node

        return True

    def pop(self):
        if self.Top is None:
            print("The stack is empty.")
            return None

        data = self.Top.data

        temp = self.Top
        self.Top = self.Top.Next
        temp.Next = None

        return data

    def peek(self):
        if self.Top is None:
            print("The stack is empty.")
            return None

        return self.Top.data

    def make_copy(self):
        copied_stack = Stack_linkedlist()

        if self.Top is None:
            return copied_stack

        values = []
        temp = self.Top

        while temp is not None:
            values.append(temp.data)
            temp = temp.Next

        for value in reversed(values):
            copied_stack.push(value)

        return copied_stack

    def is_empty(self):
        return self.Top is None

    def get_size(self):
        count = 0
        temp = self.Top

        while temp is not None:
            count += 1
            temp = temp.Next

        return count

    def search(self, item):
        position = 0
        temp = self.Top

        while temp is not None:
            if temp.data == item:
                return position

            temp = temp.Next
            position += 1

        return -1

    def display(self):
        if self.Top is None:
            print("The stack is empty.")
            return

        print("Stack elements:")

        temp = self.Top

        while temp is not None:
            print(temp.data)
            temp = temp.Next

    def clear(self):
        self.Top = None

    def __len__(self):
        return self.get_size()
