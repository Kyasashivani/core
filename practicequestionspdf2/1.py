class Students:
    total_students=0
    pass_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Students.total_students+=1

    def passing(self):
        if self.marks>Students.pass_marks:
            print("pass")
        else:
            print("Fali")
    def increase(self,a):
        self.marks+=self.marks*a/100
        print(f"marks increased to {self.marks}")
    @staticmethod
    def grade(marks):
        if marks>=80:
            return "A"
        elif marks>=60 and marks<80:
            return "B"
        else:
            return "C"

s1=Students("shivani",80)
s2=Students("sanjitha",45)
print(Students.total_students)
s1.increase(10)
s2.increase(20)
print(Students.grade(s1.marks))
print(Students.grade(s2.marks))