# define a Dog class
class Dog:

    species = "canine"                  # 'constants' for all dog objects
    legs = 4
    has_tail = True
    
    def __init__(self, name, age ):     # incoming parameters when creating dog
        self.name   = name
        self.age    = age
        
        self.tricks = []                # empty list, but not passed-in
        
    def add_trick(self, trick):         # method to add items to the list
        self.tricks.append(trick)

    def printDoggy(self):               # method to print stuff
        print(f"My name's {self.name}. I am a {self.species} ")
        print(f"I can do {len(self.tricks)} tricks ; {self.tricks} \n\n")

# - - - - - - - - - - - - - - - - 

# create 2 dog objects
d1 = Dog("Fido", 4 )
d2 = Dog("Bully", 6 )

# add tricks which dog_1 can do
d1.add_trick("shake hands")
d1.add_trick("roll over")
d1.add_trick("play dead")
d1.add_trick("skip a rope")

# add tricks dog_2 can do
d2.add_trick("fetch")
d2.add_trick("play dead")

# use the class method to print dog info
d1.printDoggy()

d2.printDoggy()


