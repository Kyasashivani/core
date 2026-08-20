class Product:
    base_tax_rate=25
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        if Product.check(self.base_price):
            final=self.base_price+(self.base_price* Product.base_tax_rate/100)
            return final
        else:
            return "Invalid amount"
    @classmethod
    def change(cls,new_tax):
        cls.base_tax_rate=new_tax
    @staticmethod
    def check(base_price):
        return base_price>0

p1=Product("shivani",10000)
p2=Product("sanjitha",20000)
print(Product.final_price(p1))
print(Product.final_price(p2))
Product.change(10)
print(Product.final_price(p1))
print(Product.final_price(p2))
print(Product.check(100))
print(Product.check(-100))
