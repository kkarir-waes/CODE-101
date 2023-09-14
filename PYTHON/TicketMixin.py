

class TicketMixin():
    ''' Mixin to calculate ticket price based on age '''

    def __init__(self, age):
        self.age = age
        print(f"age = {age}")
        self.calculate_ticket_price(age)

    def calculate_ticket_price(self, age):
        if self.age < 12:
            ticket_price = 0
        elif self.age < 18 :
            ticket_price = 15
        elif age < 60 :
            ticket_price = 20
        else:
            ticket_price = 10

        print(f"Ticket price = {ticket_price}")


class   Cost(TicketMixin):
    ''' Get the ticket price '''

    def __init___(self, age):
        '''   '''
        TicketMixin.__init__(self, age)

        print(f"Ticket price = {ticket_price}")


t1 = Cost(2)
print(t1.age)


