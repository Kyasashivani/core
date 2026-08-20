def fun(*args):
    for i in args:
        yield i**2


m=fun(1,2,3,4,5,6)
for i in m:
    print(i)