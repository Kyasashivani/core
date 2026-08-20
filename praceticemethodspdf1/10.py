class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>Student.passing_marks:
            print("Pass")
        else:
            print("Fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>80:
            return "A"
        elif marks<80 and marks>60:
            return "B"
        else:
            return "C"
s1=Student("shivani",45)
s2=Student("sanjitha",50)
s1.result()
s2.result()
Student.update_passing_marks(50)
s1.result()
s2.result()
print(f"Student name: {s1.name} and grade is: {Student.grade_category(s1.marks)}")
print(f"student name: {s2.name} and grade is {Student.grade_category(s2.marks)}")