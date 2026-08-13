from models.node import Node
class Linkedlist:
    def __init__(self):
        self.Head = None
    def append(self, item):
        New_node = Node(item)
        if self.Head is None:
            self.Head = New_node
            return
        temp = self.Head
        while temp.Next is not None:
            temp = temp.Next
        temp.Next = New_node
    def display(self):
        if self.Head is None:
            print("the linked is empty")
            return
        temp  = self.Head
        while temp is not None:
            print(temp.data)
            temp = temp.Next   


    def addafter(self,item,after):
        if self.Head is None:
            print("the linked is emtpy")
            return
        New_node = Node(item)
        temp = self.Head
        while temp.data !=after:
            temp = temp.Next
        if temp.data == after and temp.Next is None:
            temp.Next  =New_node
            return
        New_node.Next = temp.Next
        temp.Next  = New_node   


    def addat(self,item,index):
            if self.Head is None:
                print("none")
                return
            temp = self.Head
            New_node = Node(item)
            number_Node = self.get_size(temp)+1
            if index <=number_Node:
                if index ==1:
                    New_node.Next = self.Head
                    self.Head = New_node
                    return
                if index ==number_Node:
                    while temp.Next != None:
                        temp = temp.Next
                    temp.Next = New_node
                    return
                counter = 1
                while index -1 != counter:
                    temp = temp.Next
                    counter+=1
                New_node.Next = temp.Next
                temp.Next = New_node
            else:
                print("the index that you take it is bigger than the size of the linkedlist")

    def get_size(self, mnode):
            if mnode is None:
                return 0 
            return 1+self.get_size(mnode.Next)
    ####################################################################
    
    def deletefirst(self):
        if self.Head is None:
            print("list is empty")
            return
        temp = self.Head
        self.Head = temp.Next
        temp.Next = None
    #######################################################################
    def deletelast(self):
        if self.Head is None:
            print("list is empty")
            return
        elif self.Head.Next is None:
            self.Head =None
            return
        temp = self.Head
        while temp.Next.Next is not None:
            temp = temp.Next
        temp.Next = None
    ##########################################################################
    def get_length(self):
        if self.Head is None:
            return 0
        couter = 0
        temp = self.Head
        while temp is not None:
            couter+=1
            temp = temp.Next
        return couter

    #############################################################################
    def find(self,item):
        if self.Head is None:
            return None
        temp = self.Head
        while temp is not None:
            if temp.Data ==item:
                break
            temp = temp.Next
        return temp
#     ######################################
    def findAt(self,position):
        if self.Head is None:
            return None
        if position > self.get_length():
            print("out of bound.....")
            return None
        couter = 0
        temp = self.Head
        while temp is not None:
            couter+=1
            if temp.data ==couter:
                break
            temp = temp.Next
        return temp
    
    def delete_Data(self,item):
        if self.Head is None:
            print("the linked is None")
            return
        temp = self.Head
        if self.Head.data == item:
            t = self.Head
            self.Head = self.Head.Next
            t.Next =None
            return
        while temp.Next.data !=item:
            temp = temp.Next
        if temp.Next.Next is None:
            temp.Next = None
            return
        t = temp.Next
        temp.Next = temp.Next.Next
        t.Next = None




    def delete_index(self,index):
        if self.Head is None:
            print("the linked is None")
            return
        temp = self.Head
        if index <= self.get_size(temp):
            if index == 1:
                t = self.Head
                self.Head = self.Head.Next
                t.Next = None
                return
            counter = 1
            while index-1 !=counter:
                temp = temp.Next
                counter+=1
            if temp.Next.Next is None:
                temp.Next = None
                return
            t = temp.Next
            temp.Next = temp.Next.Next
            t.Next = None
        else:
            print("out of the range")
   
      def l(self,end):
      	if            
      def  deleteuntil(int item):
      	if self.Head is None:
      		print("list is empty")
            return
          temp = self.Head (input ("enter the "))
          if self.Head.data == item:
            t = self.Head
            self.Head = self.Head.Next
      	while temp.Next.Next is not None:
      	   temp = temp.Next
          temp.Next = None
          
          