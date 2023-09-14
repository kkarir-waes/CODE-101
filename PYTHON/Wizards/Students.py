class Student():
    ''' Initialise Student object '''
    def __init__(self, name, gender):
        self.name = name            # _name will not go through the setter validation        
        self.gender = gender        # _gender bypasses setter validation

    def __str__(self):
        return f"Student: {self.name} is {self.gender}"


    # Class method for creating the object 
    @classmethod
    def get(cls):
        name = input("Student name : ")
        gender = input("Gender : ")
        return cls(name.capitalize(), gender.lower())


    # Getter / setter for name attribute 
    @property                   
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is required")
        self._name = name


    # Getter and setter properties for gender, with validation 
    @property       
    def gender(self):
        return self._gender
    
    @gender.setter  
    def gender(self,gender):
        if gender not in ("M", "m","F",  "f"):
            raise ValueError("Gender not valid")
        self._gender = gender



def main():
    # use the get method to get details of new student    
    student = Student.get()
    print(student)

    # instantiate objects directly, without going thru class method rules
    print("adding harry")
    harry = Student("Harry", "m")
    print(harry)


    '''
    print("updating name")    
    student.name = ""           # cuases error, cos name can't be blank
    print("updated name")
    print(student)
    '''
    

    '''
    print("adding Ron")
    ron = Student("Ron", "H")       # causes value error, due to gender
    print(ron)
    '''

if __name__ == "__main__":
    main()
