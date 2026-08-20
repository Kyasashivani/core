class Swiggy:
    users={}
    def __init__(self,name,username,age,gender,password,location):
        self.name=name
        self.username=username
        self.age=age
        self.gender=gender
        self.password=password
        self.location=location
        self.cart=[]
        self.orders=[]
        self.logged=False
        Swiggy.users[username]=self

    @staticmethod
    def valid(password):
        if len(password)<8:
            print("Password should contain minimum 8 characters")
            return
        upper=list(filter(lambda x:x.isupper(),password))
        digit=list(filter(lambda x:x.isdigit(),password))
        special=list(filter(lambda x:x in "!@#$%^&*",password))

        if not upper:
            print("One upper needed")
            return
        if not digit:
            print("One digit needed")
            return
        if not special:
            print("One special needed")
            return
        return password

    @classmethod
    def signup(cls):
        name=input("enter your name: ")
        while True:
            username=input("enter your username: ")
            if username in cls.users:
                print("Username already exists.")
                continue
            else:
                break
        while True:
            password=input("Enter your password: ")
            if cls.valid(password):
                break
        age=int(input("enter your age: "))
        gender=input("enter your gender: ")
        location=input("Enter you location: ")
        return cls(name,username,age,gender,password,location)

    def login(self):

        print("\n--- Login for", self.name, "---")

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == self.username and password == self.password:
            self.logged = True
            print("Login successful")
        else:
            print("Invalid username or password")
    def menu(self):
        if not self.logged:
            print("Please login")
            return
        print("\n swiggy menu")
        print("1.Biryani-250rs")
        print("2.Pizz- 300rs")
        print("3.Burger - 150rs")
        print("Fried Rice - 180")
        print("Dosa - 100")
    def addtocart(self):
        if not self.logged:
            print("Please login")
            return

        self.menu()

        choice = input("Enter your food: ")

        if not choice.isdigit():
            print("Please enter a number from 1 to 5")
            return

        choice = int(choice)

        food = {
            1: ("Biryani", 250),
            2: ("Pizza", 300),
            3: ("Burger", 150),
            4: ("Fried Rice", 180),
            5: ("Dosa", 100)
        }

        if choice in food:
            item = food[choice]
            self.cart.append(item)
            print(f"{item[0]} added to your cart")
        else:
            print("Invalid food choice")

    def view_cart(self):
        if not self.logged:
            print("Please login")
            return
        if not self.cart:
            print("your cart is empty")
            return
        total=0
        for i,item in enumerate(self.cart):
            print(f"{i+1}.{item[0]}-{item[1]}")
            total+=item[1]
        print(f"Total amount: {total}")
s1=Swiggy.signup()
s2=Swiggy.signup()
#s3=Swiggy.signup()
s1.login()
s2.login()
print("\n========== USER 1 CART ==========")

s1.addtocart()
s1.addtocart()
s1.view_cart()

print("\n========== USER 2 CART ==========")


s2.addtocart()
s2.addtocart()
s2.view_cart()