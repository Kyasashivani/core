class Employee:
    company_name="Techcorps"
    def __init__(self,name):
        self.name=name

    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
        print(f"My new company was: {cls.company_name}")

    def display(self):
        print(f"name: {self.name}")
        print(f"My before company was: {Employee.company_name}")


e1=Employee("shivani")
e2=Employee("sanjitha")
print("Before changing company: ")
e1.display()
e2.display()
Employee.change_company("capgemini")
print("after changing company: ")
e1.display()
e2.display()


