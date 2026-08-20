def fun(x):
    for i in x:
        if i in "aeiouAEIOU":
            yield i

m=fun("shivani")
print(next(m))
print(next(m))
print(next(m))