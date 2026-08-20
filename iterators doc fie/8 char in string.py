class String:
    def __init__(self,s):
        self.s=s
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.s):
            i=self.index
            self.index+=1
            return self.s[i]
        raise StopIteration

s1=String("shivani")
for i in s1:
    print(i)