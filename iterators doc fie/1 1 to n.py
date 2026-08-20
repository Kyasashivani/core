class Number:
    def __init__(self,n):
        self.n=n
        self.index=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<=self.n:
            s=self.index
            self.index+=1
            return s
        raise StopIteration
num=Number(10)
for i in num:
    print(i)