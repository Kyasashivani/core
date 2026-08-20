class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def increment_salary(self,amount):
        self.salary+=amount
        return f"new salary was: {self.salary}"

e1=Employee(1,"shivani",20000)
print(e1.increment_salary(20000))