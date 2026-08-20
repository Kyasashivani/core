class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>40:
            return True
        else:
            return False
s1=Student("shivani",50)
s2=Student("sanjitha",30)
if s1.is_passed():
    print("Passed")
else:
    print("Failed")
if s2.is_passed():
    print("Passed")
else:
    print("Failed")
def is_passed(self):
    return self.marks>40
s=[Student("shivani",30),
   Student("sanjitha",22),
   Student("kalyani",60),]
for stu in s:
    if stu.is_passed():
        print("passed")
    else:
        print("Failed")