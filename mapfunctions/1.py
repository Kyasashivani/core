from functools import reduce
n1=[[1,2],[3,4],[5,6]]
m=list(map(lambda x: x+[5],n1))
print(m)


m1={"apple": 100,"banana": 40,"cherry": 150}
f=list(filter(lambda x: m1[x]>50,m1))
print(f)


l=[1,2,5,4,6,8]
r=reduce(lambda x,y:x if x>y else y,l)
print(r)

n2="SHIVANI"
m=list(map(lambda x:ord(x),n2))
print(m)

n3="shivani"
f=list(filter(lambda x:x not in "aeiou",n3))
print(f)

c=['P', 'y', 't', 'h', 'o', 'n']
r=reduce(lambda x,y:x+y,c)
print(r)

s= [10, 350, 10, 350, 20]
m=list(map(lambda x: id(x),s))
print(m)

l1=[5, 10, 15, 20, 25, 30]
m=list(map(lambda x:x**2,l1))
f=list(filter(lambda x:x%5==0,m))
print(f)
r=reduce(lambda x,y:x+y,f)
print(r)
o=reduce(lambda x,y:x+y,list(filter(lambda x:x%5==0,list(map(lambda x: x**2,l1)))))
print(o)