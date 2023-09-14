
class Car:
	def __init__(self, color, make, model, fueltype):
		self.color = color
		self.make = make
		self.model = model
		self.fueltype = fueltype



bullitt = Car('Green', 'Ford', 'Mustang', 'Gasoline')
trotter = Car('Yellow', 'Leyland', 'Triumph', 'Petrol')

print(bullitt.color)
print(trotter.model)

# --------------------------------------------
# adding a method / function
# --------------------------------------------

class Bird:
   """
   Bird class
   """
   def __init__(self, kind, call):
      #properties
       self.kind = kind
       self.call = call

   #behaviour
   def description(self):
       """
       describe the bird
       """
       return f"A {self.kind} goes {self.call}" 
       
owl = Bird('Owl', 'Twit Twoo!')
print(owl.description())

# --------------------------------------------
# adding a method / function
# --------------------------------------------
# Write your code here
class OrderItem:
    """ Creates an instance of OrderItem """
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
        
    def description(self):
        return f"{self.quantity} x {self.item} at ${self.price} each"
    


# The code below will use your class to print values to the terminal after 
# it has been written. Comment the lines below back in to test it  

order_item_one = OrderItem("bowtie", 10, 3)
print(order_item_one.description())

order_item_two = OrderItem("Fez", 25, 1)
print(order_item_two.description())
