from random import randint

# This is a one-line comment

"""
This is  multi-line comment.

We can spread this across as many lines as we need to
and it won't impact our computer program at all!!!
"""

def lottery_generator():
    """
    Appends ten random numbers to an empty list
    Returns the list
    """
    numbers = [] # Empty list to hold the numbers
    for number in range(0, 10):
		# randint() generates random integers
        numbers.append(randint(1, 50))
    return numbers

print(f"This weeks winning lottery numbers are {lottery_generator()}")