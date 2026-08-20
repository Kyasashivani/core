def multiply(x):
    def inner(y):
        print(x*y)
        return y
    return inner
k=multiply(25)
l=multiply(70)
print(k(30))
print(l(20))