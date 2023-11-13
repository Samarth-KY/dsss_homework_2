import random

def generate_random_int(lower_limit, upper_limit):
    """
    Generates a random integer within the specified limits.

    Parameters:
    - lower_limit (int): The lower limit of the range (inclusive).
    - upper_limit (int): The upper limit of the range (inclusive).

    Returns:
    - int: A random integer within the specified limits.
    """
    try:
        # Ensure the input limits are valid
        if not isinstance(lower_limit, int) or not isinstance(upper_limit, int):
            raise ValueError("Both lower limit and upper limit must be integers.")

        # Ensure the lower limit is less than upper limit
        if lower_limit > upper_limit:
            raise ValueError("Lower limit should be less than or equal to the upper limit.")

        # Generate and return a random integer
        return random.randint(lower_limit, upper_limit)
    
    except ValueError as input_error:
        # Display the error message
        print(f"Error: {input_error}")
        return None


def select_random_operation():
    """
    Selects a random math operation from the set {'+', '-', '*'}.

    Parameters:
    - None

    Returns:
    - str: A random math operation from the set {'+', '-', '*'}
    """
    # Select and return a math operation at random (+,- or *)
    return random.choice(['+', '-', '*'])


def math_operation(number1, number2, operator):
    """
    Performs a mathematical operation (+, -, *) on two numbers.

    Parameters:
    - number1 (int): The first operand.
    - number2 (int): The second operand.
    - operator (str): The operator to apply on the operands (+, -, *).

    Returns:
    - tuple: A tuple containing the expression string and the result of the operation.
    """
    try:
        # Ensure the input operands are valid numbers
        if not isinstance(number1, int) or not isinstance(number2, int):
            raise ValueError("Both number1 and number2 must be integer values.")

        # Perform the specified mathematical operation
        if operator == '+': 
            answer = number1 + number2
        elif operator == '-': 
            answer = number1 - number2
        elif operator == '*': 
            answer = number1 * number2
        else:
            raise ValueError("Invalid operator. Select from the set of operators {'+', '-', '*'}.")
        
        # Generate the expression string
        problem = f"{number1} {operator} {number2}"
        # Return the expression string and answer of the math operation
        return problem, answer
    
    except ValueError as input_error:
        print(f"Error: {input_error}")
        return None

def math_quiz():
    """
    Performs a Math Quiz Game.

    Parameters:
    - None

    Returns:
    - None
    """
    try:
        score = 0
        total_questions = 3 # Rounded 3.14 to 3 to ensure integer result 

        print("Welcome to the Math Quiz Game!")
        print("You will be presented with math problems, and you need to provide the correct answers.")

        for _ in range(total_questions):
            num1 = generate_random_int(1, 10); 
            num2 = generate_random_int(1, 5); # Rounded 5.5 to 5 to ensure integer result 
            operator = select_random_operation()
            problem, answer = math_operation(num1, num2, operator)

            # Print the question and get user's answer as integer
            print(f"\nQuestion: {problem}")
            user_answer = input("Your answer: ")

            try:
                    user_answer = int(user_answer)
            except ValueError:
                raise ValueError("Invalid input. Please enter a valid integer.")

            # Increment score by 1 if user gives correct answer
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
                    
            # Print the correct answer if user's answer is incorrect 
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
                
        # Display the final score
        print(f"\nGame over! Your score is: {score}/{total_questions}")
        
    except ValueError as input_error:
        print(f"Error: {input_error}")

    

if __name__ == "__main__":
    math_quiz()
