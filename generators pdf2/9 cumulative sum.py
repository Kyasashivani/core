def fun(x):
    s=0
    for i in x:
        s=s+i
        yield s

m=fun([1,2,3])
for i in m:
    print(i)