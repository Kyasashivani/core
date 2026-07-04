#What is the error if you place a positional argument after a keyword argument? Test it. 
def s(a=1,b=3,c=5):
    print(a*b*c)
s(1,2,c=3)
#s(a=1,2,3)
s(1,2,c=3)
s(1,c=5,b=6)