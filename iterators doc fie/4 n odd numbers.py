class Odd:
    def __init__(self,n):
        self.n=n
        self.index=1
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count<self.n:
            if self.index%2!=0:
                self.index+=2
                self.count+=1
                return self.index-2
        raise StopIteration

o1=Odd(5)
for i in o1:
    print(i)