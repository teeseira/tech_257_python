from libraries_modules_packages import math_operations

print(math_operations.add(5, 10))  # Example usage of add function
print(math_operations.subtract(10, 5))  # Example usage of subtract function
print(math_operations.multiply(5, 10))  # Example usage of multiply function
print(math_operations.divide(10, 5))  # Example usage of divide function

'''
import math_operations

# Function to add two numbers
def add(num1, num2):
    return math_operations.add(num1, num2)

# Function to subtract two numbers
def subtract(num1, num2):
    return math_operations.subtract(num1, num2)

# Function to multiply two numbers
def multiply(num1, num2):
    return math_operations.multiply(num1, num2)

# Function to divide two numbers
def divide(num1, num2):
    return math_operations.divide(num1, num2)

'''

'''
# Function to add two numbers

def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"

# Test cases
if __name__ == "__main__":
    # Test addition
    print("Addition:", add(5, 3))  # Output should be 8

    # Test subtraction
    print("Subtraction:", subtract(5, 3))  # Output should be 2

    # Test multiplication
    print("Multiplication:", multiply(5, 3))  # Output should be 15

    # Test division
    print("Division:", divide(6, 3))  # Output should be 2.0
    print("Division:", divide(6, 0))  # Output should be "Cannot divide by zero"
'''