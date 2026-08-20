class Subtraction:
    def __init__(self,m):
        self.m=m
    def __str__(self):
        return f"{self.m}"

    def __sub__(self,other):
        return Subtraction(self.m-other.m)
s1=Subtraction(90)
s2=Subtraction(50)
print(s1-s2)