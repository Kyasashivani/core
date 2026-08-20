class Even:
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

e1=Even([1,2,3,4,5,6,7,8,9])
for i in e1:
    #if not None:
    print(i)
class Vowel:
    def __init__(self,s):
        self.s=s
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.s):
            i=self.index
            self.index+=1
            if self.s[i] in "aeiouAEIOU":
                return self.s[i]
        else:
            raise StopIteration
v1=Vowel("shivani")
for i in v1:
    print(i,end=" ")
class Maximum:
    def __init__(self,h):
        self.h=h
        self.index=0
        self.maxi=float('-inf')
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.h):
            i=self.index
            self.index+=1
        # for i in range(len(self.h)):
            if self.h[i]>self.maxi:
                self.maxi=self.h[i]
                return self.maxi
        else:
            raise StopIteration

m1=Maximum([7,5,3,8,6,9,2,10])
for i in m1:
    print(i)
