class DeliveryService:
    @staticmethod
    def delivery_charge(amount):
        if amount>=500:
            return "Free Delivery"
        else:
            return "Delivery Charge is 50rs"
d1=DeliveryService()
print(d1.delivery_charge(1000))
print(d1.delivery_charge(300))