class Evenindex:
    def __init__(self,l):
        self.l=l
        self.index=1
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            i=self.index
            self.index+=1
            if self.index%2==0:
                return self.l[i]
        raise StopIteration

e1=Evenindex([1,5,3,9,4,8,5,8])
for i in e1:
    print(i)
