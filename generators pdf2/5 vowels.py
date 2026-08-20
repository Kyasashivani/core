def fun(x):
    for i in x:
        if i in "aeioAEIOU":
            yield i

m=fun("sri vidhya shivani kalyani")
for i in m:
    print(i)