def fun(x):
    for i in str(x):
        yield int(i)
m=fun(122345)
for i in m:
    print(i)