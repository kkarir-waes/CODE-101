# Define super class of Pets
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print(f"What am I ?")


# - Define Dog class, inheriting from Pet Class -------------
class Dog(Pet):
    def speak(self):
        print(f"Woof woof")




# Initialise variables
name = ""
dogs = []       # empty list to hold dog objects

# - Main processing starts here ------------------------------

# While user doesn't type "quit", input and store Dog objects
while name.lower().strip() != "quit":

    # input dog's name
    name = input("\nEnter dog's name \t: ")

    # if not 'quit', get other details
    if name.lower().strip() != "quit":

        age = input("Enter dog's age \t: ")

        # create and store dog object
        newDog = Dog(name, age)
        dogs.append(newDog)
        


# Print some info about the dog list
print(f"Number of dogs in list : {len(dogs)}") 

# print dog list
print("\n\n")
for dog in dogs:
    print(f"Name: {dog.name},\t Age: {dog.age}")

# print dog list using index values
print("\n\n")
for x in range(len(dogs)):
    print(f"Index : {x} \tName: {dogs[x].name},\t Age: {dogs[x].age}")





