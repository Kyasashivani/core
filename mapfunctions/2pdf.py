from functools import reduce
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
m=list(map(lambda x,y:x+y,a,b))
print(m)

nums = [12, 15, 7, 18, 20, 21, 25]
f=list(filter(lambda x:x%3!=x%5 and (x%3==0 or x%5==0),nums))
print(f)

