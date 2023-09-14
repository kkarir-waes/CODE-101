class TicketMixin:
    """ Mixin to calculate ticket price based on age """
   
    def calculate_ticket_price(self, age):
        
        ticket_price = 0
        print("age ", age )
        if age < 12:
            ticket_price = 0
        elif age < 18:
            ticket_price = 15
        elif age < 60:
            ticket_price = 20
        else:
            ticket_price = 10

        return ticket_price


class Customer(TicketMixin):
    """ Create instance of Customer """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Customer.ticket_price = TicketMixin.__init__(age)

    def describe(self):
        self.describe = f"{self.name} age {self.age} ticket price is {Customer.ticket_price}"


customer = Customer("Ryan Phillips", 52)
print(customer.age)
print(customer.name)
print(customer.ticket_price)
print(customer.describe())
