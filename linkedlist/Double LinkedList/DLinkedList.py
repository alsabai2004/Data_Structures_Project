from models.dnode import DNode


class DLinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None

    def isEmpty(self):
        return self.Head is None

    def get_size(self, mnode=None):
        if mnode is None:
            mnode = self.Head

        count = 0
        temp = mnode

        while temp is not None:
            count += 1
            temp = temp.Next

        return count

    def addFirst(self, data):
        new_node = DNode(data)

        if self.isEmpty():
            self.Head = self.Tail = new_node
            return True

        new_node.Next = self.Head
        self.Head.prav = new_node
        self.Head = new_node

        return True

    def addLast(self, data):
        new_node = DNode(data)

        if self.isEmpty():
            self.Head = self.Tail = new_node
            return True

        new_node.prav = self.Tail
        self.Tail.Next = new_node
        self.Tail = new_node

        return True

    def deleteFirst(self):
        if self.isEmpty():
            print("The list is empty.")
            return None

        deleted = self.Head

        if self.Head == self.Tail:
            self.Head = None
            self.Tail = None
        else:
            self.Head = self.Head.Next
            self.Head.prav = None
            deleted.Next = None

        return deleted.data

    def deleteLast(self):
        if self.isEmpty():
            print("The list is empty.")
            return None

        deleted = self.Tail

        if self.Head == self.Tail:
            self.Head = None
            self.Tail = None
        else:
            self.Tail = self.Tail.prav
            self.Tail.Next = None
            deleted.prav = None

        return deleted.data

    def find(self, val):
        temp = self.Head

        while temp is not None:
            if temp.data == val:
                return temp

            temp = temp.Next

        return None

    def deleteItem(self, val):
        if self.isEmpty():
            print("The list is empty.")
            return False

        node = self.find(val)

        if node is None:
            print(f"Value {val} was not found.")
            return False

        if node == self.Head:
            self.deleteFirst()
            return True

        if node == self.Tail:
            self.deleteLast()
            return True

        previous_node = node.prav
        next_node = node.Next

        previous_node.Next = next_node
        next_node.prav = previous_node

        node.Next = None
        node.prav = None

        return True

    def deleteAt(self, index):
        if self.isEmpty():
            print("The list is empty.")
            return False

        if index < 1:
            print("Index must be greater than or equal to 1.")
            return False

        size = self.get_size()

        if index > size:
            print("Index is out of range.")
            return False

        if index == 1:
            self.deleteFirst()
            return True

        if index == size:
            self.deleteLast()
            return True

        temp = self.Head

        for _ in range(index - 1):
            temp = temp.Next

        previous_node = temp.prav
        next_node = temp.Next

        previous_node.Next = next_node
        next_node.prav = previous_node

        temp.Next = None
        temp.prav = None

        return True

    def addAt(self, item, index):
        if index < 1:
            print("Index must be greater than or equal to 1.")
            return False

        if index == 1:
            return self.addFirst(item)

        if self.isEmpty():
            print("List is empty. Only index 1 is valid.")
            return False

        size = self.get_size()

        if index > size + 1:
            print("Index is out of range.")
            return False

        if index == size + 1:
            return self.addLast(item)

        temp = self.Head

        for _ in range(index - 1):
            temp = temp.Next

        new_node = DNode(item)
        previous_node = temp.prav

        new_node.prav = previous_node
        new_node.Next = temp

        previous_node.Next = new_node
        temp.prav = new_node

        return True

    def addAfter(self, item, after):
        if self.isEmpty():
            print("The list is empty.")
            return False

        temp = self.find(after)

        if temp is None:
            print(f"Value {after} was not found.")
            return False

        new_node = DNode(item)

        new_node.prav = temp
        new_node.Next = temp.Next

        if temp.Next is not None:
            temp.Next.prav = new_node
        else:
            self.Tail = new_node

        temp.Next = new_node

        return True

    def addBefore(self, item, befor):
        if self.isEmpty():
            print("The list is empty.")
            return False

        temp = self.find(befor)

        if temp is None:
            print(f"Value {befor} was not found.")
            return False

        if temp == self.Head:
            return self.addFirst(item)

        new_node = DNode(item)
        previous_node = temp.prav

        new_node.Next = temp
        new_node.prav = previous_node

        previous_node.Next = new_node
        temp.prav = new_node

        return True

    def deleteAfter(self, item):
        if self.isEmpty():
            print("The list is empty.")
            return False

        temp = self.find(item)

        if temp is None:
            print(f"Value {item} was not found.")
            return False

        if temp.Next is None:
            print("There is no node after this value.")
            return False

        node = temp.Next

        if node == self.Tail:
            self.deleteLast()
            return True

        next_node = node.Next

        temp.Next = next_node
        next_node.prav = temp

        node.Next = None
        node.prav = None

        return True

    def deleteBefore(self, item):
        if self.isEmpty():
            print("The list is empty.")
            return False

        temp = self.find(item)

        if temp is None:
            print(f"Value {item} was not found.")
            return False

        if temp.prav is None:
            print("There is no node before this value.")
            return False

        node = temp.prav

        if node == self.Head:
            self.deleteFirst()
            return True

        previous_node = node.prav

        previous_node.Next = temp
        temp.prav = previous_node

        node.Next = None
        node.prav = None

        return True

    def display(self):
        if self.isEmpty():
            print("The list is empty.")
            return

        temp = self.Head

        while temp is not None:
            print(temp.data)
            temp = temp.Next

    def display_recursive(self, mnode=None):
        if mnode is None:
            mnode = self.Head

        if mnode is None:
            return

        print(mnode.data)
        self.display_recursive(mnode.Next)

    def to_list(self):
        result = []
        temp = self.Head

        while temp is not None:
            result.append(temp.data)
            temp = temp.Next

        return result

    def reverse_to_list(self):
        result = []
        temp = self.Tail

        while temp is not None:
            result.append(temp.data)
            temp = temp.prav

        return result

    def clear(self):
        self.Head = None
        self.Tail = None

    def __len__(self):
        return self.get_size()

    def __str__(self):
        return str(self.to_list())
