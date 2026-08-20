class Inventory:
    total_items=0;threshold=20
    def __init__(self):
        self.stock={}
    def add(self,item,qty):
        if Inventory.valid(qty):
            self.stock[item]=qty
            Inventory.total_items+=1
        else:
            print("Invalid input")
    @staticmethod
    def valid(qty):
        return qty>=Inventory.threshold

    def remove(self,item):
        if item in self.stock.keys():
            self.stock.pop(item)
            Inventory.total_items-=1
        else:
            print(f"{item} notfound")
    @classmethod
    def update(cls,up):
        cls.threshold=up

    def display(self):
        print("items:Quantity")
        for i,j in self.stock.items():
            print(f"{i}:{j}")
        print(f"Minimun treshold : {Inventory.threshold}")
d1= Inventory()
d2=Inventory()
d1.add("pen",30)
d1.add("pencil",40)
d1.display()
