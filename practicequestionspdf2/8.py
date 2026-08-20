class Hotelroom:
    per_night=200
    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number=room_number
        self.nights_booked=nights_booked
        self.guest_name=guest_name
    def total(self):
        if Hotelroom.valid(self.nights_booked):
            return Hotelroom.per_night*self.nights_booked
        else:
            return "not valid"
    @classmethod
    def update(cls,up):
        cls.per_night+=up
    @staticmethod
    def valid(nights_booked):
        return nights_booked>0
h1=Hotelroom(102,2,"shivani")
print(Hotelroom.total(h1))
Hotelroom.update(300)
print(Hotelroom.total(h1))