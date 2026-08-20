class Evenlist:
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
        else:
            raise StopIteration
e1=Evenlist([1,2,5,3,6,37,5,8,10])
for i in e1:
    print(i)