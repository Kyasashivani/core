class Employee:
    mini_expe=3
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def promotion(self):
        if self.experience>Employee.mini_expe:
            if Employee.eligibility(self.department):
                print(f"{self.name} is eligible for promotion")
            else:
                print(f"{self.name} is not eligible for promotion.")
        else:
            print("minimum experience is required to get promotion")
    @classmethod
    def increase(cls,up):
        cls.mini_expe=up
    @staticmethod
    def eligibility(department):
        return department in ["hr","manager","tech"]
e1=Employee("shivani",6,"hr")
e2=Employee("kalyani",8,"senior manager")
e3=Employee("sanjitha",5,"tech")
Employee.eligibility(e1.department)
e1.promotion()
e2.promotion()
e3.promotion()
Employee.increase(6)
e1.promotion()
e2.promotion()
e3.promotion()