
# pasing functions as an argument

def print_arguments( **args ):
    """Prints the arguments"""
    print(f'The arguments are {args}')

def pass_function(function_name, **args):
    """Takes a function as an argument
    Passes the argument 'l' to the function passed in 
    """
    print("This function takes another function as an argument")
    function_name(f=args['l'])

pass_function(print_arguments, l='spam')