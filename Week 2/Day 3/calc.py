# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

#! /usr/bin/python


def calculator(input):
    if splitted_user_input[0] == "+":
        calculation = int(splitted_user_input[1]) + int(splitted_user_input[2])
    elif splitted_user_input[0] == "-":
        calculation = int(splitted_user_input[1]) - int(splitted_user_input[2])
    elif splitted_user_input[0] == "*":
        calculation = int(splitted_user_input[1]) * int(splitted_user_input[2])
    elif splitted_user_input[0] == "/":
        calculation = int(splitted_user_input[1]) / int(splitted_user_input[2])
    elif splitted_user_input[0] == "%":
        calculation = int(splitted_user_input[1]) % int(splitted_user_input[2])
    else:
        calculation = ("Please follow the provided guide and try again entering the values in the correct format.")
    return calculation

user_input = input("Welcome to the calculator beta version. \n Please enter your desired operation, ( + for addition, - for substraction \n * for multiplication, / for division and ""%"" for modus function)\n and the two numbers to calculate. Please use the following format: {operation} {operand} {operand} \nas in example: + 3 4 : ")
splitted_user_input = user_input.split(" ")

calculation = calculator(splitted_user_input)

print(calculation)