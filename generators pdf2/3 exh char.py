def fun(x):
    for i in x:
        yield i
m=fun("shivani")
for i in m:
    print(i)