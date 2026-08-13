from models.dnode import DNode
        
class DLinkedList:
    def __init__(self):
        self.Head=None
        self.Tail=None
    def isEmpty(self):
        return(self.Head is None and self.Tail is None)
    def get_size(self, mnode):
        if mnode is None:
            return 0 
        return 1+self.get_size(mnode.Next)

    def addFirst(self, data):
        New_Node = DNode(data)
        if self.isEmpty():
            self.Head=self.Tail=New_Node
            return
        New_Node.Next=self.Head
        self.Head.prav=New_Node
        self.Head=New_Node
    
    def addLast(self, data):
        New_Node = DNode(data)
        if self.isEmpty():
            self.Head=self.Tail=New_Node
            return
        New_Node.prav=self.Tail
        self.Tail.Next=New_Node
        self.Tail=New_Node
    def deleteFirst(self):
        if self.isEmpty():
            print("the list is empty")
            return
        t=self.Head
        if t.Next is None and t.prav is None:
            self.Head  = None
            self.Tail  = None
            return
        self.Head=self.Head.Next
        t.Next=None
        self.Head.prav=None
    def deleteLast(self):
        if self.isEmpty():
            print("the list is empty")
            return
        t=self.Tail
        if t.Next is None and t.prav is None:
            self.Tail  = None
            self.Head = None
            return
        self.Tail=t.prav
        self.Tail.Next=None
        t.prav=None

    def find(self, val):
        if self.isEmpty():
            print("the list is empty")
            return None
        t=self.Head
        while t is not None:
            if t.data==val:
                break
            t=t.Next
        return t
    def deleteItem(self, val):
        if self.isEmpty():
            print("the list is empty")
            return
        res=self.find(val)
        if res is not None:
            res.Next.prav=res.prav
            res.prav.Next=res.Next
            res.Next=None
            res.prav=None
            return
            
    def deleteAt(self, index):
        if self.Head is None:
            print("the linked is None")
            return
        temp = self.Head
        if index <= self.get_size(temp):
            if temp.Next is None and temp.prav is None and index == 1:
                self.Head = None
                self.Tail  =None
                return
            if index == 1:
                t = self.Head
                self.Head = self.Head.Next
                self.Head.prav = None
                t.Next = None
                return
            counter = 1
            while index-1 !=counter:
                temp = temp.Next
                counter+=1
            if temp.Next.Next is None:
                t = temp.Next
                temp.Next = None
                t.prav =None
                self.Tail  = temp
                return
            t = temp.Next
            temp.Next = temp.Next.Next
            t.Next.prav = temp
            t.Next = None
            t.prav = None
        else:
            print("out of the linked")

    def addAt(self, item,index):
        if self.Head is None:
            print("None")
            return
        temp = self.Head
        New_node =DNode(item)
        if index <=self.get_size(temp)+1:
            if index == 1:
                New_node.Next = self.Head
                self.Head.prav = New_node
                self.Head = New_node
                return
            counter = 1
            while index-1 !=counter:
                temp = temp.Next
                counter+=1
            if index-1 ==counter and temp.Next is None:
                temp.Next = New_node
                New_node.prav = temp
                self.Tail = New_node
                return
            t = temp.Next
            New_node.Next = t
            New_node.prav = temp
            temp.Next = New_node
            t.prav = New_node
        else:
            print("out of the range")




    def addAfter(self,item, after):
        if self.Head is None:
            print("the linked is emtpy")
            return
        New_node = DNode(item)
        temp = self.Head
        while temp.data !=after:
            temp = temp.Next
        if temp.data == after and temp.Next is None:
            temp.Next  =New_node
            New_node.prav = temp
            self.Tail = New_node
            return
        t = temp.Next
        New_node.Next = temp.Next
        t.prav = New_node
        New_node.prav = temp
        temp.Next  = New_node   

    def addBefore(self,item, befor):
        if self.Head is None:
            print("the linked is empty")
            return
        New_node = DNode(item)
        temp = self.Tail
        while temp.data != befor:
            temp = temp.prav
        if temp.data ==  befor and temp.prav is None:
            temp.prav = New_node
            New_node.Next = temp
            self.Head = New_node
            return
        t= temp.prav
        New_node.prav = t
        New_node.Next = temp
        temp.prav = New_node
        t.Next = New_node

    def deleteAfter(self, item):
        if self.Head is None:
            print("the linked is None")
            return
        temp = self.Head
        while temp.data !=item:
            temp = temp.Next
        if temp.Next is None:
            print("there is no node after this")
            return
        if temp.Next.Next is None:
            t = temp.Next
            temp.Next = None
            t.prav = None
            self.Tail = temp
            return
        t = temp.Next.Next
        d = temp.Next
        temp.Next = t
        t.prav = temp
        d.Next = None
        d.prav = None
        
    def deleteBefore(self,item):
        if self.Head is None:
            print("the linked is None")
            return
        temp = self.Tail
        while temp.data !=item:
            temp = temp.prav
        if temp.prav is None:
            print("there is no node after this")
            return
        if temp.prav.prav is None:
            t= temp.prav
            temp.prav = None
            t.Next = None
            self.Head = temp
            return
        t = temp.prav.prav
        d = temp.prav
        temp.prav = t
        t.Next = temp
        d.Next = None
        d.prav = None
    
    def display(self):
        t=self.Head
        while t is not None:
            print(t.data)
            t=t.Next
    def display_recursive(self,mnode):
        if mnode is None:
            return
        print(mnode.data)
        self.display_recursive(mnode.Next)
        