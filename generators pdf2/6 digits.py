def fun(x):
    for i in x:
        if i.isdigit():
            yield i
m=fun("Shivani@1234")
for i in m:
    print(i,end=" ")