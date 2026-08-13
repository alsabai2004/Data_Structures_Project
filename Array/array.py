class Arrays:
    def __init__(self, size):
        self.data = []
        self.size = size
    def insert(self):
        print("enter array elements")
        for i in range(self.size):
            self.data.append(int(input("enter the value: ")))
    def display(self):
        self.size = len(self.data)
        for i in range(self.size):
            print(self.data[i])
    def deleteitem(self, item):
        self.data.remove(item)
    def deleteALLItem(self, item):
        self.size = len(self.data)
        total_iteration = self.data.count(item)
        for i in range(total_iteration):
            self.data.remove(item)
    def notfirst(self,item):
        tota_iteration = self.data.count(item)
        the_index = self.data.index(item)
        for i in range(tota_iteration):
            if i != the_index:
                self.data.remove(item)