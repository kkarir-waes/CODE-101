#----------------------------------------------------------
# Use a class to define several constants
#----------------------------------------------------------

class myConstants:
    pi = 3.14752
    angle = 180
    radius = 15

print(f'pi     = {myConstants.pi}')
print(f'angle  = {myConstants.angle}')
print(f'radius = {myConstants.radius}')

# create an object, myPi, with a value from the Constants class
myPi = myConstants.pi
print(f'MyPi = {myPi} and is of type : {type(myPi)}')

# create an object, radius, with a value from the Constants class
radius = myConstants.radius
print(f'radius = {radius} and is of type : {type(radius)}')




#----------------------------------------------------------
# Use class to define variables and methods
#----------------------------------------------------------
class student :
    
    def name (name = "Freddy"):
        print(f'Hello {name}')
        print("It's been a long time")
        
    def place (place = "London"):
        print(f'{place} sounds like a nice place')


student.name()
student.place()
