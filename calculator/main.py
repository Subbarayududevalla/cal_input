import sys
from calculator import Calculator  # Import the Calculator class
from calculator.operations import add, subtract, multiply, divide  # Import arithmetic operations
from decimal import Decimal, InvalidOperation

def main():
    # Get user input for operands and operation
    a = Decimal(input("Enter the first number: "))
    b = Decimal(input("Enter the second number: "))
    operation = str(input("Enter the operation (+, -, *, /): "))

    # Pass all inputs to the calculate_and_print function
    calculate_and_print(a, b, operation)


def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        '+': Calculator.add,
        '-': Calculator.subtract,
        '*': Calculator.multiply,
        '/': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name)  # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:  # Catch-all for unexpected errors
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
