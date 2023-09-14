
#----------------------------------------------------------
# Use class to define a Person
#----------------------------------------------------------
class Person :
   
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        print(f'{self.name} is age {self.age}')


# create an object using the student class
grandpa = Person("Jackson", 85)
grandma = Person("Betty", 78)
mommy = Person("Charlotte", 45)
daddy = Person("Rupert", 47)

sonny = Person("Jimmy", 15)
daughter = Person("sally", 13 )


Person.printPerson(grandpa)
Person.printPerson(mommy)
Person.printPerson(sonny)
