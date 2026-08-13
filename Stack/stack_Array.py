class Stack:
    def __init__(self, maxSize):
        self.Top = -1
        self.data = [0]*maxSize
        self.MaxSize = maxSize
    def isEmpty(self):
        return self.Top == -1
    def isfull(self):
        return self.Top == self.MaxSize-1
    def push(self, item):
        if self.isfull():
            print("Stack overflow")
            return
        self.Top+=1
        self.data[self.Top]= item
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        value = self.data[self.Top]
        self.Top-=1
        return value
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        value = self.data[self.Top]
        return value
    def display(self):
        if self.isEmpty():
            print("Stack underflow")
            return
        for i in range(self.Top , -1, -1):
            print(self.data[i])
        #or
        # index = self.Top
        # while (index >=0):
        #     print(self.data[index])
        #     index -= 1
    def TransStack(self):
        if self.isEmpty():
            print("underflow")
            return
        s = Stack(self.Top+1)
        while not self.isEmpty():
            s.push(self.pop())
        s2 = Stack(s.Top+1)
        t = s
        while not s.isEmpty():
            t = s.pop()
            self.push(t)
            s2.push(t)
        return s2
    def deleteElement(self, val):
        if self.isEmpty():
            print("underflow")
            return
        s =Stack(self.Top+1)
        if val == self.peek():
            s.data[self.Top+1] =self.pop() 
        print(s.data.index(val))
        print(s.data)
        