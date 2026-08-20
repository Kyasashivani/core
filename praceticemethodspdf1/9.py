class BankAccount:
    bank_name="cv bank"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if BankAccount.valid_amount(amount):
            self.balance+=amount
            print(f"total amount was: {self.balance}")
        else:
            print("Invalid amount")
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
        return f"new bank was: {new_name}"
    @staticmethod
    def valid_amount(amount):
        return amount>0
b1=BankAccount("shivani",20000)
b2=BankAccount("sanjitha",50000)
b1.deposit(5000)
b2.deposit(-1000)
print(BankAccount.change_bank_name("varanasi bank"))