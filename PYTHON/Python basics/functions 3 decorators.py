
""" Here is a very simple decorator. 
It modifies the function say_hello by printing a string before it is called 
and after it is called. 
The decorator is modifying the behaviour of the function. 
It wraps the function and extends the behaviour of the wrapped 
function without modifying the function permanently. 
"""

def my_decorator(func):
    def wrapper():
        print("The function has not been called yet. Let's call it.")
        func()
        print("The function was called and has returned a result.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")
    
say_hello()

# -------------------------------------------------------
# By changing the argument in the decorator, 
# you can change this to acres, for example, 
# without altering the function. 
# -------------------------------------------------------

def define_units(unit):
    """Define the units"""
    def decorator_define_units(func):
        func.unit = unit
        return func
    return decorator_define_units

@define_units('m^2')
def area(length, width):
    """Calculate area of rectangle or parallelogram"""
    return length * width

# The unit defined in the decorator can be used with dot notation
# In this case the function area units can be used as area.unit
print(f'The area is {area(3,5)}{area.unit}')




# -------------------------------------------------------
# 
# -------------------------------------------------------

def add_author(func):
    """
    Decorator to add string with author information
    to print after decorated function runs
    """
    def wrapper(*args):
        r = func(*args)
        return f"{r}\nBy Code Institute"
    return wrapper
        
# write your code here
@add_author
def print_article_title(title):
    return(f"Article Title: {title}")

result = print_article_title("Python Decorators")
print(result)


