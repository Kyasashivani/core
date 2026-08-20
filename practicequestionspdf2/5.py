class Course:
    total_courses=0
    minimum=10
    def __init__(self,title, duration,enrolled_student):
        self.title=title
        self.duration=duration
        self.enrolled_student=enrolled_student
        Course.total_courses += 1
    def enroll(self):
        if Course.validate(self.duration):
            self.enrolled_student+=1
            print(f"number of students enrolled are {self.enrolled_student}")
    @classmethod
    def update(cls,up):
        cls.minimum+=up

    @staticmethod
    def validate(duration):
        return 0< duration<=1000

c1=Course("Java",20,20)
c2=Course("Python",10,30)
c3=Course("C",30,0)
print(Course.total_courses)
c1.enroll()
c2.enroll()
c3.enroll()
print(c1.enrolled_student)
print(c2.enrolled_student)
print(c3.enrolled_student)
Course.update(20)
c1.enroll()
c2.enroll()
c3.enroll()