class Instagram:
    usernames = {}
    MIN_AGE = 18

    def __init__(self, name, username, age, gender, password):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = password
        self.followers = 0
        self.following = 0
        self.friends_list = []
        self.logged = False
        Instagram.usernames[username] = self

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            print("Password must contain at least 8 characters")
            return False

        special = {"!", "@", "#", "$", "%", "&", "*"}
        upper = list(filter(lambda x: x.isupper(), password))
        special_char = list(filter(lambda x: x in special, password))
        digit = list(filter(lambda x: x.isdigit(), password))

        if not upper:
            print("Password must contain at least one uppercase letter")
            return False

        if not special_char:
            print("Password must contain at least one special character")
            return False

        if not digit:
            print("Password must contain at least one number")
            return False
        return True

    @staticmethod
    def validate_age(age):
        if age < Instagram.MIN_AGE:
            print("You must be 18 years or older to create an account")
            return False
        return True

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")
        while True:
            username = input("Enter your username: ")
            if username in cls.usernames:
                print("Username already registered. Try another one")
                continue
            break
        while True:
            password = input("Enter your password: ")
            if cls.validate_password(password):
                break
        age = int(input("Enter your age: "))
        if not cls.validate_age(age):
            print("You are not eligible to use Instagram.")
            return None
        gender = input("Enter your gender (Male/Female): ")
        return cls(name, username, age, gender, password)

    def login(self):

        print("\n--- Login for", self.name, "---")

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == self.username and password == self.password:
            self.logged = True
            print("Login successful")
        else:
            print("Invalid username or password")

    def logout(self):
        if self.logged:
            self.logged = False
            print("Logged out successfully")
        else:
            print("Already logged out")

    def follow(self, user):
        if not self.logged:
            print("Not logged in")
            return

        if user in self.friends_list:
            print("User is already following")
            return
        self.following += 1
        user.followers += 1
        self.friends_list.append(user)
        print(f"You are now following {user.name}")

    def unfollow(self, user):
        if not self.logged:
            print("Not logged in")
            return

        if user not in self.friends_list:
            print("User not Found")
            return

        self.following -= 1
        user.followers -= 1
        self.friends_list.remove(user)

        print(f"You unfollowed {user.name}")

    def profile(self):
        if not self.logged:
            print("Please login to view profile")
            return
        print(f"\n{self.name}'s Profile")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Following : {self.following}")
        print(f"Followers : {self.followers}")

    def friends_profile(self):
        if not self.logged:
            print("Not logged in")
            return

        if not self.friends_list:
            print("You are not following anyone")
            return

        print("\nPeople you are following:")

        for i, friend in enumerate(self.friends_list):
            print(f"{i} : {friend.name}")

        choice = int(input("Enter your choice: "))
        if isinstance(choice,int):
            choice = int(choice)
            if 0 <= choice < len(self.friends_list):
                self.friends_list[choice].profile()
            else:
                print("Invalid choice")
        else:
            print("please enter a number")

i1 = Instagram.signup()
i2 = Instagram.signup()
# i3 = Instagram.signup()
# i4 = Instagram.signup()

# if i1 is not None:
#     i1.login()
# if i2 is not None:
#     i2.login()
# if i3 is not None:
#     i3.login()
# if i4 is not None:
#     i4.login()
# user1 = Instagram.login()
# user2 = Instagram.login()
# user3 = Instagram.login()
# user4 = Instagram.login()
i1.login()
i2.login()
# i3.login()
# i4.login()
# if i1 is not None and i2 is not None:
#     i1.follow(i2)
# if i1 is not None and i3 is not None:
#     i1.follow(i3)
# if i1 is not None and i4 is not None:
#     i1.follow(i4)
#
# if i1 is not None:
#     i1.profile()
# if i1 is not None:
#     i1.friends_profile()
#
# if i1 is not None and i2 is not None:
#     i1.unfollow(i2)
# if i3 is not None and i2 is not None:
#     i3.follow(i2)
#
# if i3 is not None:
#     i3.friends_profile()
i1.follow(i2)
# i1.follow(i3)
# i1.follow(i4)

i1.profile()
i1.friends_profile()

i1.unfollow(i2)

# i3.follow(i2)
# i3.friends_profile()