class Queue:
    def __init__(self,size):
        self.front = -1
        self.rear = -1
        self.data = [0]*size
        self.MaxSize = size
    def is_Empty(self):
        return self.front == self.rear
    def is_full(self):
        return self.rear == self.MaxSize -1
    def reset(self):
        self.front =self.rear=-1
    def Enequeue(self,item):
        if self.is_full() and self.is_Empty():
            self.reset()
            self.rear+=1
            self.data[self.rear]= item
            return
        if self.is_full():
            print("The queue is full")
            return
        self.rear+=1
        self.data[self.rear]= item

    def dequeue(self):
        if self.is_Empty():
            if self.is_Empty() and self.is_full():
                self.reset()
                print("try another time")
                return
            else:
                print("The Queue is empty")
                return
        self.front+=1
        res = self.data[self.front]
        return res
    def get_fron(self):
        if self.is_Empty():
            print("try anotehr time")
            return
        return self.data[self.front]
    def get_rear(self):
        if self.is_Empty():
            print("try anotehr time")
            return
        return self.data[self.rear]
    def deletitem(self,item):
        if self.is_Empty():
            print("the queue is empty")
            return
        start = self.front+1
        found = False
        while (start<=self.rear):
            if self.data[start]==item:
                found = True
                index = start
                while index<self.rear:
                    self.data[index] = self.data[index+1]
                    index+=1
                self.rear-=1
            start+=1
            if found is True:
                print(self.data)
                break
    def display(self):
        if self.is_Empty():
            print("the queue is empty")
            return
        index = self.front+1
        while index <= self.rear:
            print(self.data[index])
            index+=1
        
        