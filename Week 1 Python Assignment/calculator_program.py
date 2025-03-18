# Basic Calculator Program
# Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

print("Please input two numbers and specify mathematical operation to conduct")
num1 = float(input("num1 : "))
num2 = float(input("num2 : "))

operation = int(input("\n Select a mathematical operation to conduct by typing option e.g. 1 for Addition \n"
"1. Addition \n"
"2. Subtraction \n"
"3. Multiplication \n"
"4. Division \n"))

def math_op(operation):
    match operation: # Match operation option against different cases
        case 1: # Addition
            result = num1 + num2
            return print(f'\n{num1} + {num2} = {result}')
        case 2: # Subtraction
            result = num1 - num2
            return print(f'\n{num1} - {num2} = {result}')
        case 3: # Multiplication
            result = num1 * num2
            return print(f'\n{num1} x {num2} = {result}')
        case 4: # Division
            result = num1 / num2
            return print(f'\n{num1} / {num2} = {result}')
        case _:
            return "Invalid option."
print(math_op(operation))