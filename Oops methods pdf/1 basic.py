class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks


    def display_details(self):
        print(f"name={self.name}")
        print(f"age={self.age}")
        print(f"marks={self.marks}")

s1=Student("shivani",21,99)
s2=Student("kalyani",21,100)
s1.display_details()
s2.display_details()
