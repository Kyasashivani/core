def fun(x):
    for i in range(1,x+1):
        yield i

m=fun(10)
for i in m:
    print(i)
