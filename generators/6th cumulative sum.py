def fun(*args):
    s = 0
    for i in args:
        s=s+i
        yield s

m=fun(1,2,3)
print(next(m))
print(next(m))
print(next(m))