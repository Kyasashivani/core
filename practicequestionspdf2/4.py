class Loan:
    fixed=10000
    interest_loan=2
    def __init__(self,name,principle):
        self.name=name
        self.principle=principle
    def total(self):
        if Loan.eligible(self.principle):
            t=self.principle+self.principle*Loan.interest_loan
            return t
        else:
            return "loan is not sanctioned"
    @classmethod
    def update(cls,up):
        cls.interest_loan+=up

    @staticmethod
    def eligible(principle):
        return principle>=10000

l1=Loan("shivani",20000)
l2=Loan("kalyani",10000)
print(Loan.total(l1))
print(Loan.total(l2))
Loan.update(1)
print(Loan.total(l1))
print(Loan.total(l2))