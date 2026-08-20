class MovieTicket:
    @staticmethod
    def ticket_price(age):
        if age<12:
            return "Ticket price is 100"
        elif age<=60:
            return "200"
        else:
            return "150"
m1=MovieTicket()
print(m1.ticket_price(45))
print(m1.ticket_price(11))
print(m1.ticket_price(12))
print(m1.ticket_price(70))