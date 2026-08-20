class Numbers:
    def __init__(self,n):
        self.n=n
        self.index=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=1:
            s=self.index
            self.index-=1
            return s
        raise StopIteration
num=Numbers(10)
for i in num:
    print(i)