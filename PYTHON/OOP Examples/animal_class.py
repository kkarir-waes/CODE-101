
class Animal():
    
    def __init__(self, name, age ):
        self.name = name
        self.age = age
        
    def printAnimal(self):
        print(f"Animal : {self.species}, {self.name}, {self.age}")


# - Dog Class ---------------------------------
class Dog(Animal):
    species = "canine"     # class attribute, with a fixed value
    tail = True
    
    def speak(self):
        print("woof")


# - Cat Class ------------------------------------------------------
class Cat(Animal):

    species = "feline"     # class attribute, with a fixed value
    
    def speak(self):
        print("meow")


#- Fish Class ------------------------------------------------------------
class Fish(Animal):
    species = "piscene"     # class attribute, with a fixed value

    def speak(self):
        print("glug")

# - Mian Section ------------------------------------------------
d1 = Dog("Fido", 10)
c1 = Cat("Luna", 6)
f1 = Fish("Bubbles", 1)


print(d1.species)
print(c1.species)
print(f1.species)



