"""
DESCRIPTION OF THE PROJECT

Fizz Buzz:
    1. Demo mode: Loop through a data structure containing numbers
    from 1 to 20 and print FizzBuzz result for each
    2. Ask user to input a number, tell user the FizzBuzz result
    for their chosen number in a string

FizzBuzz rules:
    - if a number is divisible by 3, return "Fizz"
    - if a number is divisible by 5, return "Buzz"
    - if a number is divisible by both 3 and 5, return "FizzBuzz"
    - if a number is not divisible by either 3 or 5, return the number.
"""


def fizz_buzz(n):
    """
    Calculate FizzBuzz answer
    """
    if n % 3 == 0 and n % 5 == 0:
        answer = "FizzBuzz"
    elif n % 3 == 0:
        answer = "Fizz"
    elif n % 5 == 0:
        answer = "Buzz"
    else:
        answer = n
    return answer


def demo_mode():
    """
    Loop through a list of numbers and print a string to show 
    the result for each item
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
            12, 13, 14, 15, 16, 17, 18, 19, 20]
    for num in nums:
        print(f"The result for {num} is {fizz_buzz(num)}")


def input_mode():
    """
    Get user's input, return string to tell them the FizzBuzz result
    """
    number = int(input("Choose a number: "))
    result = fizz_buzz(number)
    print(f"The result for {number} is {result}")
    play_again()


def play():
    """
    Explain modes and let user choose
    """
    print("FizzBuzz is a game to help children learn division.")
    print("If a number is divisible by 3, it returns 'Fizz'.")
    print("If a number is divisible by 5, it returns 'Buzz'.")
    print("If a number is divisible by 3 and 5, the result is 'FizzBuzz'.")
    print("Here is a demo:")
    demo_mode()
    print("Try it yourself!")
    input_mode()


def play_again():
    """
    Allow user to play again
    """
    print("Do you want to try another number?")
    again = input("Press Y for yes, or any other key to exit: ")
    if again.lower() == "y":
        input_mode()
    else:
        print("Goodbye!")


print("Hi there, welcome to FizzBuzz!")
play()
