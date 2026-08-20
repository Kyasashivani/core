class Reverse:
    def __init__(self,s):
        self.s=s
        self.index=len(s)-1
    def __iter__(self):
        return self
    def __next__(self):
        while self.index>=0:
            i=self.index
            self.index-=1
            return self.s[i]
        raise StopIteration
r1=Reverse("shivani")
for i in r1:
    print(i)