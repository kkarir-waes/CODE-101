import random

class Hat:
    '''
        Example of @ClassMethod class

        There will not be any instantitaion of a Hat object.
        but we can treat it as a function, with its own data

    NB: No 'self,  but 'cls' as we are refering to THIS class

    '''

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in ", random.choice(cls.houses))

#------- MAIN -----------------------------------
def main():
    Hat.sort("Harry")
    Hat.sort("Ron")
    Hat.sort("Ginny")

if __name__ == "__main__":
    main()
