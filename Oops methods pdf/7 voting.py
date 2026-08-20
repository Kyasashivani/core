class Voting:
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age
    # def voting_eligible(self,age):
    #     if Voting.is_eligible(age):
    #         print("Eligible to Vote")
    #     else:
    #         print("Not Eligible")
    @staticmethod
    def is_eligible(age):
        if age>=18:
            # return age
            print("eligible")
        else:
            print("not eligible")

v1=Voting()
v1.is_eligible(21)
# v2=Voting("shivani",17)
# v2.voting_eligible(v2.age)