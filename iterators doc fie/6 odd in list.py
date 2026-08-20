class Oddlist:
    def __init__(self,l):
        self.l=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            i=self.index
            self.index+=1
            if self.l[i]%2==1:
                return self.l[i]
        raise StopIteration
o1=Oddlist([1,2,3,4,5,6,7,8,9])
for i in o1:
    print(i)