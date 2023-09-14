def print_message(name):
    print(f"Hello {name}")

username = input("What's your name? ")
print_message(username)

# ------------------------------
# with default value
# ------------------------------


def print_message(name="World"):
    return f"Hello {name}"

username = input("What's your name? ")
print(print_message())
print(print_message(username))


# ------------------------------
# passing a tuple and an int
# ------------------------------

def add_numbers(nums_tuple, min_value):
    sum = 0
    j = 0
    for i in nums_tuple:
        if nums_tuple[j] >= min_value:
            sum += nums_tuple[j]
        j += 1
    return(sum)
        
total = add_numbers( (21, 4,7,19,1), 15)
print(total)

# ------------------------------
# with default value
# ------------------------------
