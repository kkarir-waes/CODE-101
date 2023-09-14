
# - Define Person class -------------------------------------
class Person:

    def __init__(self, name, address, age, course):
        self.name = name
        self.address = address
        self.age = age
        self.course = course


# - Define Student class -------------------------------------
class Student(Person):

    def __init__(self, name, address, age, course, house_name):
        super().__init__(name, address, age, course)
        self.house_name = house_name
        
    def greeting(self):
        print(f"Hi, I'm {self.name} and I'm studying {self.course}" )
        print(f"I belong to {self.house_name} \n\n" )


# - Define Teacher class -------------------------------------
class Teacher(Person):

    def greeting(self):
        print(f"Hi, I'm Professor {self.name} and I teach {self.course}" )


# - Main processing starts here -------------------------------------

t1 = Teacher("Snape", "Hogwarts", 50, "Defence Against the Dark Arts")
s1 = Student("Harry", "Cupboard Under the Stairs", 11, "Wizardry", "Gryffindor")
s2 = Student("Ron", "The Burrow", 11, "Potions", "Gryffindor")
s3 = Student("Draco", "Hammer Palace", 12, "Dark Arts", "Slytherin")

print("\n\n")
t1.greeting()

print("\n\n")
s1.greeting()
s2.greeting()
s3.greeting()
