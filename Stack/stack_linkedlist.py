from models.node import Node
class Stack_linkedlist:
    def __init__(self):
        self.Top = None
    
    def push(self, item):
        item= Node(item)
        if self.Top == None:
            self.Top = item
            return
        item.Next = self.Top
        self.Top = item
    def pop(self):
        if self.Top is None:
            print("the Stack is empty")
            return
        data = self.Top.data
        temp = self.Top
        self.Top = self.Top.Next
        temp.Next = None
        return data
    def peek(self):
        if self.Top is None:
            print("there is no Peek")
            return
        return self.Top.data
    def make_copy(self):
        if self.Top is None:
            print("error")
            return
        s = Stack_linkedlist()
        while self.Top  is not None:
            s.push(self.pop())
        s2 = Stack_linkedlist()
        d = s.pop()
        while d !=None:
            s2.push(d)
            self.push(d)
            d= s.pop()
        return s2
    

        