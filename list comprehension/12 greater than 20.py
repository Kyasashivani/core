numbers = [10, 15, 20, 25, 30, 35]
gen=(i for i in numbers if i>20)
for i in gen:
    print(i)