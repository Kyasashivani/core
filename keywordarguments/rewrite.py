#Rewrite this call using keyword arguments: book_ticket('Alice', 'Delhi', 'Mumbai', 2)
def book_ticket(name,place,to,nof):
    print(f"{name} {place},{to},{nof}")
book_ticket(name="Alice",to="Mumbai",nof=2,place="Delhi")