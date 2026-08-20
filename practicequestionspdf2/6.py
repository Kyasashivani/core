class Vehicle:
    service_charge_rate=500
    def __init__(self, model, kilometers_run, service_history):
        self.model=model
        self.kilometers_run=kilometers_run
        self.service_history=service_history
    def charge(self):
        if Vehicle.eligible(self.model):
            return Vehicle.service_charge_rate* self.kilometers_run
        else:
            return "not eligible"
    @classmethod
    def update(cls,up):
        cls.service_charge_rate+=up
        print(f"vehicle service rate is updated to {cls.service_charge_rate}")

    @staticmethod
    def eligible(model):
        current=2026
        age=current-model
        return age<=15
v1=Vehicle(2018,35,5)
v2=Vehicle(2000,15,10)
print(f"vehicle charge of model {v1.model} is {Vehicle.charge(v1)}")
Vehicle.update(200)
print(f"vehicle charge of model {v2.model} is {Vehicle.charge(v2)}")

