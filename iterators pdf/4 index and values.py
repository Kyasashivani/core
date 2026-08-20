class List:
    def __init__(self,l):
        self.l=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            i=self.index
            self.index+=1
            return i,self.l[i]
        raise StopIteration

l1=List([1,2,3,4])
for i in l1:
    print(i)