def run_twice(func,value):
    return func(func(value))
def cube(a):
    return a**3
def square(a):
    return a*a
print(run_twice(cube,3))    #19683
print(run_twice(square,3))  #81