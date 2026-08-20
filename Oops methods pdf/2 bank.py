class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        if BankAccount.valid(amount):
            self.balance+=amount
            return self.balance
        else:
            return "not valid amount"

    @staticmethod
    def valid(amount):
        if amount>0:
            return amount

b1=BankAccount("shivani",20000)
print(b1.deposit(2000))

