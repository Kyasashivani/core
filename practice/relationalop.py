class Relation:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __gt__(self,other):
        return Relation(self.a>other.a)
    def __str__(self):
        return f"{self.a},{self.b}"

r1=Relation(20,30)
r2=Relation(40,20)
print(r1>r2)