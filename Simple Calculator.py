import math

# To store history of calculations
history = []

# Functions for operations
def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    result = x - y
    return result

def multiply(x, y):
    result = x * y
    return result

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by 0"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(x)

# Display calculator menu
def display_menu():
    print("\n=== Simple Python Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Show History")
    print("8. Exit")

# Main calculator loop
def calculator():
    while True:
        display_menu()
        choice = input("Choose an option (1-8): ")

        if choice == '8':
            print("Thank you for using the calculator!")
            break

        elif choice == '7':
            print("\n--- Calculation History ---")
            for h in history:
                print(h)
            if not history:
                print("No history yet.")
            continue

        elif choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                op = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                op = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                op = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                op = f"{num1} / {num2} = {result}"
            elif choice == '5':
                result = power(num1, num2)
                op = f"{num1} ^ {num2} = {result}"

        elif choice == '6':
            try:
                num = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue

            result = square_root(num)
            op = f"√{num} = {result}"

        else:
            print("Invalid choice. Please select a valid option.")
            continue

        print("Result:", result)
        history.append(op)

# Run the calculator
calculator()
