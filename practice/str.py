class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x},{self.y}"
    def __repr__(self):
        return f"x={self.x},y={self.y}"
p1=Point(3,5)
print(p1)
print(repr(p1))