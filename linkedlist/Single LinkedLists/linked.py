from models.node import Node


class Linkedlist:
    def __init__(self):
        self.Head = None

    def is_empty(self):
        return self.Head is None

    def append(self, item):
        new_node = Node(item)

        if self.Head is None:
            self.Head = new_node
            return True

        temp = self.Head

        while temp.Next is not None:
            temp = temp.Next

        temp.Next = new_node
        return True

    def display(self):
        if self.Head is None:
            print("The linked list is empty.")
            return

        temp = self.Head

        while temp is not None:
            print(temp.data)
            temp = temp.Next

    def addafter(self, item, after):
        if self.Head is None:
            print("The linked list is empty.")
            return False

        temp = self.Head

        while temp is not None:
            if temp.data == after:
                new_node = Node(item)
                new_node.Next = temp.Next
                temp.Next = new_node
                return True

            temp = temp.Next

        print(f"Value {after} was not found.")
        return False

    def addat(self, item, index):
        if index < 1:
            print("Index must start from 1.")
            return False

        if index == 1:
            new_node = Node(item)
            new_node.Next = self.Head
            self.Head = new_node
            return True

        if self.Head is None:
            print("The linked list is empty.")
            return False

        temp = self.Head
        counter = 1

        while temp is not None and counter < index - 1:
            temp = temp.Next
            counter += 1

        if temp is None:
            print("Index out of range.")
            return False

        new_node = Node(item)
        new_node.Next = temp.Next
        temp.Next = new_node

        return True

    def get_size(self, mnode=None):
        if mnode is None:
            mnode = self.Head

        count = 0
        temp = mnode

        while temp is not None:
            count += 1
            temp = temp.Next

        return count

    def get_length(self):
        return self.get_size()

    def deletefirst(self):
        if self.Head is None:
            print("List is empty.")
            return False

        temp = self.Head
        self.Head = self.Head.Next
        temp.Next = None

        return True

    def deletelast(self):
        if self.Head is None:
            print("List is empty.")
            return False

        if self.Head.Next is None:
            self.Head = None
            return True

        temp = self.Head

        while temp.Next.Next is not None:
            temp = temp.Next

        temp.Next = None
        return True

    def find(self, item):
        temp = self.Head

        while temp is not None:
            if temp.data == item:
                return temp

            temp = temp.Next

        return None

    def findAt(self, position):
        if position < 1:
            print("Position must start from 1.")
            return None

        temp = self.Head
        counter = 1

        while temp is not None:
            if counter == position:
                return temp

            temp = temp.Next
            counter += 1

        print("Position out of range.")
        return None

    def delete_Data(self, item):
        if self.Head is None:
            print("The linked list is empty.")
            return False

        if self.Head.data == item:
            return self.deletefirst()

        temp = self.Head

        while temp.Next is not None:
            if temp.Next.data == item:
                node = temp.Next
                temp.Next = node.Next
                node.Next = None
                return True

            temp = temp.Next

        print(f"Value {item} was not found.")
        return False

    def delete_index(self, index):
        if self.Head is None:
            print("The linked list is empty.")
            return False

        if index < 1:
            print("Index must start from 1.")
            return False

        if index == 1:
            return self.deletefirst()

        temp = self.Head
        counter = 1

        while temp.Next is not None and counter < index - 1:
            temp = temp.Next
            counter += 1

        if temp.Next is None:
            print("Index out of range.")
            return False

        node = temp.Next
        temp.Next = node.Next
        node.Next = None

        return True

    def deleteuntil(self, item):
        if self.Head is None:
            print("List is empty.")
            return False

        while self.Head is not None and self.Head.data != item:
            self.deletefirst()

        if self.Head is None:
            print(f"Value {item} was not found.")
            return False

        return True

    def clear(self):
        self.Head = None

    def to_list(self):
        result = []
        temp = self.Head

        while temp is not None:
            result.append(temp.data)
            temp = temp.Next

        return result

    def __len__(self):
        return self.get_size()

    def __str__(self):
        return str(self.to_list())
