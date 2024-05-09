# Prompt the user to enter their name
name = input("Enter your name: ")

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2

# Check if num2 is not 0 to avoid division by zero
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "Undefined (division by zero)"

# Print personalized greeting and results
print("Hello, {name}!\n")
print("Addition Result: {num1} + {num2} = {addition_result}")
print("Subtraction Result: {num1} - {num2} = {subtraction_result}")
print("Multiplication Result: {num1} * {num2} = {multiplication_result}")
print("Division Result: {num1} / {num2} = {division_result}")