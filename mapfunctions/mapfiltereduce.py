from functools import reduce
sales = [
 {"item": "Pen", "price": 10, "qty": 5},
 {"item": "Bag", "price": 500, "qty": 0},
 {"item": "Book", "price": 120, "qty": 3},
 {"item": "Eraser", "price": 5, "qty": 10},
 ]
# f=list(filter(lambda x:x["qty"]>0,sales))
# print(f)
# m=list(map(lambda x:x["price"]*x["qty"],f))
r=reduce(lambda x,y:x+y,list(map(lambda x:x["price"]*x["qty"],list(filter(lambda x:x["qty"]>0,sales)))))
print(r)


students = [
 {"name": "Ravi", "score": 45},
 {"name": "Sneha", "score": 78},
 {"name": "Kiran", "score": 60},
 {"name": "Divya", "score": 92}
]
f=list(filter(lambda x:x["score"]>=60,students))
m=list(map(lambda x:x|{"grade":"Pass"},f))
s=sorted(m,key=lambda x:x["score"],reverse=True)
print(s)

logs = [
 "09:15 [INFO] Server started",
 "13:42 [ERROR] Disk full",
 "11:50 [ERROR] Timeout",
 "15:03 [INFO] Request OK",
 "14:20 [ERROR] DB connection lost",
]
f=list(filter(lambda x:"ERROR" in x,logs))
print(f)