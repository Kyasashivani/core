class Member:
    BMI_limit=20
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

    def calculate(self):
        if self.tool(self.height,self.weight):
            bmi=self.weight/self.height**2
            if bmi>Member.BMI_limit:
                return "not fit"
            else:
                return "fit"

        return "height and weight must be positive."
        # return None
    @classmethod
    def update(cls,up):
        cls.BMI_limit=up
    @staticmethod
    def tool(height,weight):
        return height>0 and weight>0

m1=Member("shivani",1.1,30)
m2=Member("kalyani",5.5,45)
print(f"{m1.name} is {Member.calculate(m1)}")
print(f"{m2.name} is {Member.calculate(m2)}")
Member.update(40)
print(f"{m1.name} is {Member.calculate(m1)}")
print(f"{m2.name} is {Member.calculate(m2)}")

