import random

def generate_random_number(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Returns a random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """
    Generates a math problem string and calculates the answer based on the operator.
    Parameters:
    - num1: First number
    - num2: Second number
    - operator: Mathematical operator

    Returns:
    - problem_str: A string representation of the problem
    - correct_answer: The correct answer for the problem
    """
    problem_str = f"{num1} {operator} {num2}"
    
    # Calculate the correct answer
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:  # operator == '*'
        correct_answer = num1 * num2
    
    return problem_str, correct_answer

def math_quiz():
    """
    Starts a math quiz game where the user answers generated math problems.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the number of questions
    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)
        operator = generate_random_operator()

        # Generate the problem and the answer
        problem, correct_answer = create_math_problem(num1, num2, operator)
        
        print(f"\nQuestion: {problem}")
        
        # Handle invalid input from the user
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  # Skip to the next question

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
