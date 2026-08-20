class Employee:
    company="Infosys"
    @classmethod
    def change_company(cls,new):
        cls.company=new
        return new
e1=Employee()
print(e1.company)
e1.change_company("google")
print(e1.company)