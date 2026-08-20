class Course:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name
        #Course.total_students += 1
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print(f"total students:{cls.total_students}")
    @staticmethod
    def is_eligible(age):
        if age>=18:
            return True
        else:
            return False
c1=Course("shivani")
c2=Course("sanjitha")
c3=Course("saipriya")
c1.enroll()
c2.enroll()
c3.enroll()
Course.show_total()
print(Course.is_eligible(25))
print(Course.is_eligible(12))
Course.show_total()