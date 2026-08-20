from itertools import count


class Even:
    def __init__(self,n):
        self.n=n
        self.index=0
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count<self.n:
            if self.index%2==0:
                self.index+=2
                self.count+=1
                return self.index-2
            # else:
            #     return self.index+1
        raise StopIteration
n=Even(5)
for i in n:
    print(i)
