def fun(x):
    for i in str(x):
        yield int(i)

m=fun(12345)
print(m)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))