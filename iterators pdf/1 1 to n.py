class Numbers:
    def __init__(self,n):
        self.n=n
        self.index=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<self.n:
            i=self.index
            self.index+=1
            return i
        raise StopIteration
n1=Numbers(10)
for i in n1:
    print(i)