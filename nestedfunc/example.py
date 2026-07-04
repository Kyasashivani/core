# def add(x,y):
#     def display(x,y):
#         print(x,y)
#     display(x,y)
# add(10,20)
#L E G B : L local, E Enclosed, G Global, B Built-in.
# z=70
# def fun():
#     x=30
#     def fun2():
#         y=50
#         print(y,x,z)
#     fun2()
# fun()
'''x=600
def fun():
    x=200
    def fun2():
        nonlocal x
        def fun3():
            nonlocal x
            x=100
            print(x)
        fun3()
    print(x)
    fun2()
    print(x)
fun()
print(x)'''

n=6543
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
ree=0
c=0
while rev>0:
    r=rev%10
    ree=ree*10+r
    c+=1
    if c>1:
        print(end=" + ")
    print(ree,end="")
    rev=rev//10