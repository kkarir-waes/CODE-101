questions = [
    {
    "question": "What is the capital of Spain?",
    "correct": 2
    }, 
    {
    "question": "What is the capital of Argentina?",
    "correct": 1
    }, 
    {
    "question": "What is the capital of Ireland?",
    "correct": 0
    }
    ]


def quiz():
    """
    Play quiz:
    - get user's name
    - trigger the ask_question function
    - print result when every question has been asked
    """
    score = 0
    name = input("Hello, what is your name? ")
    print(f"Hi {name}! Welcome to the quiz. Good luck!")
    for question in questions:
        score = ask_question(question, score)
        
    print(f"{name}, you scored {score} out of {len(questions)}")


def ask_question(dictionary, score):
    """
    Ask question:
    - display question
    - display answers
    - check answer
    - give feedback
    - update score
    - return score to pass back to quiz function for next iteration
    """
    print(dictionary["question"])
    answer_number = 1
    answers = ["Dublin", "Buenos Aires", "Madrid", "San Juan"]
    
    for answer in answers:
        print(f"{answer_number} {answer}")
        answer_number += 1
        
    user_answer = int(input("Your answer (please enter a number): "))
    
    if user_answer - 1  == dictionary["correct"]:
        print("Well done, that was the correct answer!")
        score += 1
    else:
        print("Sorry, that was not the correct answer.")
    #    score += 1
    return score


quiz()
