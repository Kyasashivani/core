class Car:
    wheels=4
    def __init__(self,milage):
        self.milage=milage

    def display_specs(self):
        print(f"milage: {self.milage}")
        print(f"wheels : {self.wheels}")
    @classmethod
    def change(cls,w):
        cls.wheels=w
        print(f"update wheels: {w}")

c1=Car("high")
c2=Car("low")
c1.change(8)
c2.change(10)
c1.display_specs()
c2.display_specs()