def fun(x):
    c=len(x)-1
    while c>=0:
        yield x[c]
        c=c-1
m=fun("shivani")
for i in m:
    print(i)