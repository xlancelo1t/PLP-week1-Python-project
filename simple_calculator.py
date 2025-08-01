# Step 1: Ask the user to input the first number
num1 = float(input("Enter the first number: "))  # I am using float to allow decimal inputs

# Step 2: Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Step 3: Ask the user to choose a mathematical operation
operation = input("Enter the operation (+, -, *, /): ")

# Step 4: Perform calculation based on the chosen operation
if operation == '+':
    result = num1 + num2  # Addition
    print(f"{num1} + {num2} = {result}")
# Step 5: Handle other operations

elif operation == '-':
    result = num1 - num2  # Subtraction
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2  # Multiplication
    print(f"{num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:  # Check to avoid division by zero
        result = num1 / num2  # Division
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    # If the user entered an invalid operation
    print("Invalid operation. Please enter +, -, *, or /.")
