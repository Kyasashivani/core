class Even:
    def __init__(self,l):
        self.l=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            i=self.index
            self.index+=1
            if self.l[i]%2==0:
                return self.l[i]
        raise StopIteration
e1=Even([2,3,5,3,6,8,7])
for i in e1:
    print(i)