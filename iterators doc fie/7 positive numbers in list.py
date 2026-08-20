class Positive:
    def __init__(self,l):
        self.l=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            i=self.index
            self.index+=1
            if self.l[i]>0:
                return self.l[i]
        raise StopIteration
p1=Positive([6,3,6,-1,-3,-5,-6,7,8])
for i in p1:
    print(i)