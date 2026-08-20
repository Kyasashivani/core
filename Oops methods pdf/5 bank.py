class Bank:
    bank_name="SBI"
    @classmethod
    def change_bank(cls,new):
        cls.bank_name=new
        print(f"Then new bank name: {new}")
b1=Bank()
print(f"The old bank name: {b1.bank_name}")
print(f"The old bank name: {Bank.bank_name}")
b1.change_bank("HDFC")