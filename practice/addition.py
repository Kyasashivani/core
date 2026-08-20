class Addition:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Addition(self.x+other.x,self.y+other.y)

    def __str__(self):
        return f"({self.x}),({self.y})"
    
a1=Addition(10,20)
a2=Addition(30,40)
print(a1+a2)